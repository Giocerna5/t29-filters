import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import numpy as np
import cv2

UPLOAD_FOLDER = 'videos'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mov'])

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/home')
def home():
    return render_template('template.html')

#@app.route('/page2')
#def page2func():
 #  return render_template('page2.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Editor</title>
    <h1>Upload File to edit</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
@app.route('/uploads/<filename>')
def uploaded_file(filename):

    cap = cv2.VideoCapture('filename')

    while(cap.isOpened()):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return render_template('page2.html')
    #two buttons for editor and  filter choice
    #
