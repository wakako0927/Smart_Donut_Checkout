from flask import Flask, render_template, request, redirect, url_for
import os
from utils.donut_detector import detect_donuts

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect(request.url)

    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    result = detect_donuts(filepath)
    return render_template('result.html', result=result, image_path=filepath)

if __name__ == '__main__':
    app.run(debug=True)
