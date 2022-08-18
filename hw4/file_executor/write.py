import os

def write_to_file(file, body):
    if os.path.isfile(f"{file}"):
        with open(f"{file}", 'w') as file1:
            file1.write(f"{body}")
            file1.close()
        print(f"Text: '{body}' writed в {file}")
    else:
        print("File not found!”")
