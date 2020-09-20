import fnmatch
import os
from typing import List


def read_character_files(file_names: List[str]) -> str:
    entries = ''

    file_names = resolve_all_files(file_names)

    for file_name in file_names:
        entries = entries + load_from_file(file_name)

    return entries


def resolve_all_files(file_names):
    if len(file_names) == 1 and file_names[0] == 'all':
        file_names = [os.path.splitext(file)[0] for file in
                      os.listdir(os.path.join(os.path.dirname(__file__), "data"))
                      if fnmatch.fnmatch(file, "*.csv")]
    return file_names


def load_from_file(file_name: str) -> str:
    provided_file = os.path.join(os.path.dirname(__file__), "data", file_name + '.csv')
    if os.path.isfile(file_name):
        actual_file_name = file_name
    elif os.path.isfile(provided_file):
        actual_file_name = provided_file
    else:
        raise FileNotFoundError(f"Couldn't find file {file_name}")

    with open(actual_file_name, "r") as file:
        return file.read()
