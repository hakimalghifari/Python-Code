import os

file_path = "try.txt"

if os.path.exists("try.txt"):
    os.remove(file_path)
    print("file " + file_path + "deleted")
else:
    print("file not exist")

