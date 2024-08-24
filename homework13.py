#!/bin/python3

import os

def get_size(path):
    kb = 0

    if os.path.isfile(path):
       kb = os.path.getsize(path)

    else:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                home = os.path.join(dirpath, filename)
                if os.path.isfile(home):
                   kb += os.path.getsize(home)
    return kb

def human_readable_size(kb):
    for abb in ['B', 'KB', 'MB', 'GB', 'TB']:
       if kb < 1024:
          break
       kb /= 1024
    return "{:.0f}{}".format(kb, abb)

def main():
    pwd = os.getcwd()
    list = os.listdir(pwd)
    size_list = []
    for item in list:
        home = os.path.join(pwd, item)
        kb = get_size(home)
        size_list.append((kb, item))

    size_list.sort(key=lambda x: x[0], reverse=True)

    for kb, item in size_list:
        print("{}\t{}".format(human_readable_size(kb), item))

if __name__ == "__main__":
    main()
