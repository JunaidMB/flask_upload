import os
from werkzeug.utils import secure_filename
from PIL import Image
from flask import Flask, flash, request, redirect, send_file, render_template, send_from_directory


UPLOAD_FOLDER = 'uploads/'

app = Flask(__name__, template_folder= 'templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def process_image(filename):
    original_image = Image.open(filename)
    rotated_image = original_image.transpose(Image.ROTATE_90)
    return rotated_image


# Define a POST method to upload the file
@app.route('/uploadfile', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('no filename')
            return redirect(request.url)
        else:
            filename = secure_filename(file.filename)
            file = process_image(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.seek(0)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            print('saved file successfully')
            print('this is the ' + filename)
        
        # send file name as parameter to download
            return redirect('/downloadfile/' + filename)
    
    return render_template('upload_file.html')

# API for downloading the file
@app.route('/downloadfile/<filename>', methods = ['GET'])
def download_file(filename):
    return render_template('download.html', value = filename)

# Download file redirects to return files
@app.route('/return-files/<filename>')
def return_files(filename):
    file_path = UPLOAD_FOLDER + filename # Destination for downloads
    return send_file(file_path, as_attachment=True, attachment_filename='', cache_timeout=0)
    
if __name__ == "__main___":
    app.run()


















