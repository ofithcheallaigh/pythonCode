import os
from os import rename, listdir

file_start = "file"
i = 1

# list directories
dir_list = os.listdir(os.getcwd())
list_dir = listdir('.')

for names in dir_list:
    if names.startswith(file_start):
        rename(names,names.replace("file","test"))

