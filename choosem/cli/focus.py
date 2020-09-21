import json
import subprocess

import click

from choosem.utils import choose


@click.command()
def focus():
    """focus a program window"""
    windows = subprocess.run(
        ['yabai', '-m', 'query', '--windows'],
        capture_output=True).stdout.decode()
    windows = json.loads(windows)
    choice = choose('\n'.join([f"{w['app']}: {w['title']}" for w in windows if w.get('title')]), index=True)
    choice = windows[choice]
    subprocess.run(['yabai', '-m', 'window', '--focus', str(choice["id"])])
