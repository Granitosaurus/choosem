import subprocess
from typing import List

import click
import pkg_resources
from choosem.utils import choose


@click.command()
@click.argument('files', nargs=-1)
@click.option('--list', 'list_files', is_flag=True)
@click.option('--switch', 'file_switch', is_flag=True)
def insert(files, list_files, file_switch):
    """insert character into active window"""
    if not files:
        files = ['emojis']
    if list_files or file_switch:
        EMOJI_FILES = [v.split('.csv')[0] for v in pkg_resources.resource_listdir('choosem', 'data')]
        if list_files:
            click.echo('\n'.join(EMOJI_FILES))
            return

    def choose_character(char_files: List[str]):
        characters = '\n'.join(
            pkg_resources.resource_string('choosem', f'data/{file}.csv').decode() for file in char_files
        )
        choices = characters
        if file_switch:
            choices += '\n'.join(EMOJI_FILES)
        choice = choose(choices)
        choice = choice.split(' ', 1)[0]
        if not choice:
            return
        if choice in EMOJI_FILES:
            return choose_character([choice])
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

    choose_character(files)
