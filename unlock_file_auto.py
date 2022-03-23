#!/usr/bin/bash
print("unclock acces set 777")
import os
os.system("chmod -R 777 /path/home")
print("files_and_folders-ok")
os.system("chmod 777 /path/hometest.py")
print("files-ok")
os.system("chmod -R 777 /dev/sdd")
print("files_and_folders-ok")
print("all done !")