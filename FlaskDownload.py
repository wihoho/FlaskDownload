from os import listdir

from flask import Flask, render_template, send_from_directory

from FlaskFile import FlaskFile

app = Flask(__name__)
folder = "/Users/wihoho/Github/FlaskDownload/static"


@app.route('/')
def hello_world():
    originalFiles = readFiles()
    afterFiles = [FlaskFile("/" + f, f) for f in originalFiles]

    return render_template("front.html", files=afterFiles)


@app.route("/<file_name>")
def getFile(file_name):
    return send_from_directory(folder, file_name, as_attachment=True)


def readFiles():
    files = listdir(folder)
    return files


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
