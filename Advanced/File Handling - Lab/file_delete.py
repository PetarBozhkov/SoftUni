4. File Delete

Create a program that deletes the file you created in the previous task. If you try to delete the file multiple times, print the message: 'File already deleted!'.

from os import remove
from os.path import exists

file_path = './file_to_delete.txt'

# open(file_path, 'w').close()
if exists(file_path):
    remove(file_path)
    print('File Deleted!')
else:
    print('File already deleted!')
