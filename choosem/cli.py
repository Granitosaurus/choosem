import json
import shlex
import subprocess
from typing import Union
from pathlib import Path

import click

from choosem.emoji import read_character_files


def choose(inp, index=False) -> Union[str, int]:
    """
    open choose command with a given input
    values should be \n separated

    Keyword Args:
        index: whether to return index of chosen value rather than the value itself
            this is useful when there's a possibility of non-unique names
    """
    cmd = ['choose', '-m']
    if index:
        cmd.append('-i')
    try:
        choice = subprocess.run(
            cmd,
            input=inp,
            encoding='utf',
            capture_output=True
        ).stdout
    except ValueError:
        return -1
    return int(choice) if index else choice


@click.group()
def main():
    pass


@main.command()
def emoji():
    emojis = read_character_files(['emojis'])
    choice = choose(emojis)
    choice = choice.split(' ', 1)[0]
    script = f"""
    set temp to the clipboard
    set the clipboard to "{choice}"
    tell application "System Events"
        keystroke "v" using command down
    end tell
    delay 0.5
    set the clipboard to temp
    """
    subprocess.run(f"""
        osascript -e '{script}'
    """, shell=True)


@main.command()
def launch():
    apps = Path('/Applications').glob('*/Contents/MacOS/*')
    apps = {app.stem: app for app in apps}
    choice = choose('\n'.join(apps))
    if choice in apps:
        subprocess.Popen([apps[choice]])
    else:
        args = shlex.split(choice)
        print(args)
        subprocess.Popen(args)


@main.command()
def focus():
    """focus a window by selection"""
    # Use a breakpoint in the code line below to debug your script.
    windows = subprocess.run(
        ['yabai', '-m', 'query', '--windows'],
        capture_output=True).stdout.decode()
    windows = json.loads(windows)
    choice = choose('\n'.join([f"{w['app']}: {w['title']}" for w in windows if w.get('title')]), index=True)
    choice = windows[choice]
    subprocess.run(['yabai', '-m', 'window', '--focus', str(choice["id"])])


if __name__ == '__main__':
    main()
