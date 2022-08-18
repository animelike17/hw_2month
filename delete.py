import os

def delete_file(file):
    if os.path.isfile(f"{file}"):
        os.remove(f"{file}")
        print(f"File {file} deleted!!!")
    else:
        print(f"File not found!”")

