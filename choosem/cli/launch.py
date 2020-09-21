import shlex
import subprocess
from pathlib import Path

import click
from choosem.utils import choose


@click.command()
def launch():
    """launch application"""
    apps = Path('/Applications').glob('*/Contents/MacOS/*')
    apps = {app.stem: app for app in apps}
    choice = choose('\n'.join(apps))
    if choice in apps:
        subprocess.Popen([apps[choice]])
    else:
        args = shlex.split(choice)
        subprocess.Popen(args)
