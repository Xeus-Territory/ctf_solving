from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/heyyou', methods = ['GET', 'POST'])
def setcookie():
    resp = make_response(render_template('miracle.html'))
    resp.set_cookie('miracle', 'FLAGFLAGFLAG') 
    return resp
    
app.run(port=19969)