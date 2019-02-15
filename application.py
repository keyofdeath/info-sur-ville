from flask import Flask, make_response, jsonify, request
import wikipedia
import os
import logging.handlers

PYTHON_LOGGER = logging.getLogger(__name__)
if not os.path.exists("log"):
    os.mkdir("log")
HDLR = logging.handlers.TimedRotatingFileHandler("log/application.log",
                                                 when="midnight", backupCount=60)
STREAM_HDLR = logging.StreamHandler()
FORMATTER = logging.Formatter("%(asctime)s %(filename)s [%(levelname)s] %(message)s")
HDLR.setFormatter(FORMATTER)
STREAM_HDLR.setFormatter(FORMATTER)
PYTHON_LOGGER.addHandler(HDLR)
PYTHON_LOGGER.addHandler(STREAM_HDLR)
PYTHON_LOGGER.setLevel(logging.DEBUG)

# Absolute path to the folder location of this python file
FOLDER_ABSOLUTE_PATH = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))


app = Flask(__name__)


@app.route('/', methods=["POST"])
def homepage():

    if request.json and 'wikipedia' in request.json:
        try:
            text = request.json["wikipedia"]
            PYTHON_LOGGER.info("Get request for: {}".format(text))
            wikipedia.set_lang("fr")
            res = {"summary": wikipedia.summary(text)}
            return make_response(jsonify(res), 200)
        except Exception as e:
            return make_response(jsonify({"error": "Error in the request"}), 400)
