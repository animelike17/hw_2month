import os
from pathlib import Path

def create_file(file_name, extension):
    if os.path.isfile(f"{file_name}{extension}"):
        print('File not found!”')
    else:
        position = open(f"{file_name}{extension}", 'w')
        position.close()
        print(Path(f"{file_name}{extension}").absolute())

