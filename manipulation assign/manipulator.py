import shutil
import os

def read_file(file_path):
     with open(file_path, 'r') as file:
          content = file.read()
          return content
     
print(read_file("sample.txt"))

# Task 3
def write_to_file(file_path, text_to_write):
        with open(file_path, 'a') as file:
            file.write(text_to_write)
text = "Additional line added for file operations"
write_to_file("sample.txt", text)

# Task 5
shutil.move("sample.txt", "Files")

# Task 7
os.rename('file1.txt','renamed_file.txt')

# Task 8
def search_and_erase(file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} has been erased.")
        else:
            print(f"{file_path} does not exist.")

search_and_erase("file2.txt")

# Task 9
def find_files_and_folders(path):
    for files in os.walk(path):
     
        print("Files:")
        for file in files:
            print((file))
        print("--------------------------------------")

find_files_and_folders("Files")


# Task 10


shutil.make_archive('archive','zip','Files')