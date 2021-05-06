import os
from zipfile import ZipFile
from os.path import basename

import os
arr = os.listdir()
print(arr)


def zip_files(zipfilename, directoryname):
    files = os.listdir(os.path.join("./", directoryname))
    relevant_files = files[1::]

    zipObj = ZipFile(os.path.join("./uploads", zipfilename), 'w')
    for filename in relevant_files:
        filePath = os.path.join("./uploads", filename)
        zipObj.write(filePath, basename(filePath))
    zipObj.close()


zip_files(zipfilename = "rotated.zip", directoryname = "uploads/")

import os, glob

os.getcwd()
dir = UPLOAD_FOLDER
for file in os.scandir(dir):
    os.remove(file.path)

for i in os.scandir(os.getcwd() + "/" + "uploads/"):
    print(i.path)

def clean_directory(dir):
    for file in os.scandir(dir):
        os.remove(file.path)

clean_directory(dir = UPLOAD_FOLDER)
