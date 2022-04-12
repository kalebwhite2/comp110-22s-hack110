import math
import os
from flask import Flask, flash, render_template, request, redirect, url_for
from helpers import Uploaded_Image, categorize_images
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
all_uploads: list[Uploaded_Image] = []

app: Flask = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/freaky-fire-escapes")
def freaky_fire_escapes():
    return render_template('/pages/freaky_fire_escapes.html', all_uploads=categorize_images(all_uploads, 'freaky_fire_escapes'), rows=math.ceil(len(categorize_images(all_uploads, 'freaky_fire_escapes')) / 3), length=len(categorize_images(all_uploads, 'freaky_fire_escapes')))

@app.route("/stupid_study_spots")
def stupid_study_spots():
    return render_template('/pages/stupid_study_spots.html', all_uploads=categorize_images(all_uploads, 'stupid_study_spots'), rows=math.ceil(len(categorize_images(all_uploads, 'stupid_study_spots')) / 3), length=len(categorize_images(all_uploads, 'stupid_study_spots')))

@app.route("/badass_bathrooms")
def badass_bathrooms():
    return render_template('/pages/badass_bathrooms.html', all_uploads=categorize_images(all_uploads, 'badass_bathrooms'), rows=math.ceil(len(categorize_images(all_uploads, 'badass_bathrooms')) / 3), length=len(categorize_images(all_uploads, 'badass_bathrooms')))

@app.route("/funky_fire_spots")
def funky_fire_spots():
    return render_template('/pages/funky_fire_spots.html', all_uploads=categorize_images(all_uploads, 'funky_fire_spots'), rows=math.ceil(len(categorize_images(all_uploads, 'funky_fire_spots')) / 3), length=len(categorize_images(all_uploads, 'funky_fire_spots')))

@app.route("/crazy_coffee")
def crazy_coffee():
    return render_template('/pages/crazy_coffee.html', all_uploads=categorize_images(all_uploads, 'crazy_coffee'), rows=math.ceil(len(categorize_images(all_uploads, 'crazy_coffee')) / 3), length=len(categorize_images(all_uploads, 'crazy_coffee')))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return redirect(request.url)
        
        file = request.files["file"]
        description = request.form['description']
        location = request.form['location']
        section = request.form['section']
        file_location = UPLOAD_FOLDER + '/' + file.filename

        new_image: Uploaded_Image = Uploaded_Image(section, file_location, location, description)
        all_uploads.append(new_image)

        if not (description != '' and location != '' and section != ''):
            return render_template('/pages/upload.html')

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return render_template('/pages/upload_success.html')

    elif request.method == 'GET':
        return render_template('/pages/upload.html')
    else:
        return render_template('/pages/upload.html')

if __name__ == '__main__':
    app.run(debug=True)