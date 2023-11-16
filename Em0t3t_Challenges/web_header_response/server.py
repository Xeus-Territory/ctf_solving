from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/heyyou', methods = ['GET', 'POST'])
def setcookie():
    resp = make_response(render_template('miracle.html'))
    resp.set_cookie('miracle', 'em0t3t{dGgxc19jMDBrMTNfMXNfbTFyNGNsM18xbl9teXN0M3J5}') 
    return resp

app.run('192.168.11.2',port=8080)