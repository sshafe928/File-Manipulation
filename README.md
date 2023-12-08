# File and Folder Operations Assignment

This assignment involves performing various file and folder operations using Python. The objective is to demonstrate proficiency in handling files and folders through a series of tasks.


## Authors

- [@sshafe928](https://github.com/sshafe928)


### Tasks

```python
# Task 2: Read File Content

import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content

print(read_file("sample.txt"))

This code reads the content of the "sample.txt" file and prints it to the console.

# Task 3: Append Text to File

import os

def write_to_file(file_path, text_to_write):
    with open(file_path, 'a') as file:
        file.write(text_to_write)

text = "Additional line added for file operations"
write_to_file("sample.txt", text)
This code appends additional text to the "sample.txt" file.

# Task 5: Move File to Folder

import shutil

shutil.move("sample.txt", "Files")
This code moves the "sample.txt" file to a folder named "Files".

Task 7: Rename File
python
Copy code
import os

os.rename('file1.txt', 'renamed_file.txt')
This code renames "file1.txt" to "renamed_file.txt".

# Task 8: Delete File

import os

def search_and_erase(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} has been erased.")
    else:
        print(f"{file_path} does not exist.")

search_and_erase("file2.txt")
This code deletes the "file2.txt" file.

# Task 9: List Files in Folder

import os

def find_files_and_folders(path):
    for root, dirs, files in os.walk(path):
        print("Files:")
        for file in files:
            print(os.path.join(root, file))
        print("--------------------------------------")

find_files_and_folders("Files")
This code lists all files in the "Files" folder.

# Task 10: Zip Folder

import shutil

shutil.make_archive('archive', 'zip', 'Files')
This code zips the entire "Files" folder into a compressed file named "archive.zip".



