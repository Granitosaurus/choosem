import click

from choosem.cli.focus import focus
from choosem.cli.insert import insert
from choosem.cli.launch import launch


@click.group()
def main():
    pass


main.add_command(insert)


@main.group()
def yabai():
    """control yabai windows manager"""
    pass


yabai.add_command(launch)
yabai.add_command(focus)

if __name__ == '__main__':
    main()
