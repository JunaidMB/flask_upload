from app import app

import os
from werkzeug.utils import secure_filename
from PIL import Image
from flask import Flask, flash, request, redirect, send_file, render_template, send_from_directory
import io
from zipfile import ZipFile
from os.path import basename
from io import StringIO, BytesIO
from app.utils import *
from app.model.srcnn import * 


# Define a POST method to upload the file
@app.route('/uploadfile', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)
        #file = request.files['file']
        # Obtain a list of files uploaded
        files = request.files.getlist("file")
        # if user does not select file, browser also
        # submit a empty part without filename
        if not files:
            print('no filename')
            return redirect(request.url)
        else:
            # Clean the directory of any existing files
            clean_directory(dir = app.config['UPLOAD_FOLDER'])
            
            for file in files:
                filename = secure_filename(file.filename)

                # Save the original file
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                # Rotate the image
                processed_file = process_image(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                
                # Save the processed image
                processed_file.seek(0)
                processed_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Save the files to a zip file - It looks within the directory in which it is
            zip_files(zipfilename = "rotated.zip", directoryname = app.config['UPLOAD_FOLDER'])

            print('saved file successfully')
            
        
        # send file name as parameter to download html
            filename = "rotated.zip"
            print('this is the ' + filename)
            return redirect('/downloadfile/' + filename)
    
    return render_template('upload_templates/upload_file.html')

# API for downloading the file
@app.route('/downloadfile/<filename>', methods = ['GET'])
def download_file(filename):
    return render_template('download_templates/download.html', value = filename)

# Download file redirects to return files
@app.route('/return-files/<filename>')
def return_files(filename):
    file_path = app.config['UPLOAD_FOLDER'] + filename
    #file_path = 'uploads/' + filename
    return send_file(file_path, as_attachment=True, attachment_filename='', cache_timeout=0)