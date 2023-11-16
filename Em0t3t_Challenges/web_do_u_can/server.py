from os import abort
from flask import Flask, render_template, request
from builtins import open as _, eval as _a
from unicodedata import normalize as _b
from re import search as _e

app = Flask(__name__)

def check_regex(pattern):
    if _e("[\\101-\\132\\141-\\172]", pattern):
        return False
    else:
        return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/server')
def viewpath():
    return render_template('source.html')

@app.errorhandler(500)
def internal_err(error):
    return '<code> You reach to much closest, try again with some suspect parameters for bypass this</code><br><code><h2>TypeError: The view function did not return a valid response. The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a TextIOWrapper.</h2></code>'

@app.route('/payload')
def get_flag():
    if _e("[\\101-\\132\\141-\\172]", __ := _b("\116\106\113\104",request.args.get('cmd'))):
        return "/\/[]† 13@|) ßL|† \|/Я°/\/6"
    return _a(__)[0]

app.run()