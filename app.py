import flask
import numpy as np
import cv2
import pytesseract
import io

app = flask.Flask(__name__, template_folder='template')

def read_img(img):
    pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"
    text = pytesseract.image_to_string(img)
    return(text)

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('/index.html'))
    if flask.request.method == 'POST':
        myFile = flask.request.form['myFile']
        image_stream = io.BytesIO(myFile)
        image_stream.seek(0)
        file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        label = read_img(frame)
        return flask.render_template('/index.html', result=label)

if __name__ == '__main__':
    app.run()