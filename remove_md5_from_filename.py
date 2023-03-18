# This script was an automation to remove the trailing MD5 hash from my Notion exports. 
# I had a lot of files so I quickly coded this to clean it up

import os
import re

def remove_md5(filename):
    pattern = re.compile("([a-fA-F\d]{32})")
    name_list = filename.split(' ')
    ext = ''

    if not pattern.search(filename):
        return filename

    for i in range(len(name_list)):
        if pattern.search(name_list[i]):
            j = name_list[i].find('.')

            if j != -1:
                ext = name_list[i][j:]

    return ' '.join(name_list[0:i] + name_list[i+1::]) + ext


def change_names(path):
    print(path)
    for current_dir, subdirs, files in os.walk(path):
        # rename current working directory
        os.rename(current_dir, remove_md5(current_dir))
        current_dir = remove_md5(current_dir) + "/"


        # Directories
        for dirname in subdirs:
            new_dirname = remove_md5(dirname) + "/"
            os.rename(current_dir + dirname, current_dir + new_dirname)
            # recursively rename files
            change_names(current_dir + new_dirname)


        # Files
        for filename in files:
            os.rename(current_dir + filename, current_dir + remove_md5(filename))


change_names("/tmp/base folder name")


