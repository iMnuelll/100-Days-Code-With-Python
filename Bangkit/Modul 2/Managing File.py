import os

dir = "./100-Days-Code-with-Python"

for name in os.listdir(dir) :
    """
    os.listdir() -> List the directories and files in the desired directory
    """
    fullname = os.path.join(dir, name)
    """
    os.path.join() -> Combines the directory path that has been initialized in the dir variable with the directory/file name in the name variable
    """
    if os.path.isdir(fullname):
         print("{} is a directory".format(fullname))
    else:
         print("{} is a file".format(fullname))