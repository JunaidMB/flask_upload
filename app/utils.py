import os
from werkzeug.utils import secure_filename
from PIL import Image
import io
from zipfile import ZipFile
from os.path import basename
from io import StringIO, BytesIO


# Rotates images
def process_image(filename):
    original_image = Image.open(filename)
    rotated_image = original_image.transpose(Image.ROTATE_90)
    return rotated_image

def process_image_file(file):
    original_image = Image.open(io.BytesIO(file.read()))
    rotated_image = original_image.transpose(Image.ROTATE_90)
    return rotated_image

# Cleans all files from a directory
def clean_directory(dir):
    for file in os.scandir(dir):
        os.remove(file.path)

# Zips all files in the current directory and saves the zip file in the same directory
def zip_files(zipfilename, directoryname):
    files = os.listdir(os.path.join("./", directoryname))
    relevant_files = files[::]

    zipObj = ZipFile(os.path.join("./app/uploads", zipfilename), 'w')
    for filename in relevant_files:
        filePath = os.path.join("./app/uploads", filename)
        zipObj.write(filePath, basename(filePath))
    zipObj.close()