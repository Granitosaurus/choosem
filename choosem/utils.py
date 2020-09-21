import subprocess
from typing import Union


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
