import requests
import json
import sqlite3
from flask import Flask, render_template, request

# Connect DB
con = sqlite3.connect('data.db', check_same_thread=False)
app = Flask(__name__)

cur = con.cursor()

# Init DB
cur.execute('''DROP TABLE IF EXISTS titok_ids''')
cur.execute('''CREATE TABLE titok_ids (titok_id text)''')
cur.execute(
    '''INSERT INTO titok_ids (titok_id) VALUES ("my_idol_titok_id") '''
)

def checkTitokID(id='hoaa.hanassii'):
    jsonStr = requests.get('https://www.tiktok.com/oembed?url=https://www.tiktok.com/@'+str(id)).text

    try:
        # Parse json string
        pythonObj = json.loads(jsonStr)
    except:
        return False

    try: 
        code = pythonObj['code']
        if code == 400:
            # ID Not Found!
            return False
    except:
        # ID Found!
        return True

@app.route('/', methods=['GET', 'POST'])
def login():
    titokID = 'hoaa.hanassii'
    send = "index.html"

    if request.method == 'POST':

        titok_id = request.form['titok_id'].lower()

        rows = []
        try:
            cur.execute("SELECT * FROM titok_ids WHERE titok_id='" + titok_id + "'")
            rows = cur.fetchall()
        except:
            pass
	
        if len(rows) > 0:
            if checkTitokID(titok_id):
                return render_template('index.html', error="Yes, this is my idol!!!", titokID=titok_id)
            else:
                return render_template('index.html', error="Yes, this is my idol!!!", titokID='haha@haha@haha')
        else:
            if checkTitokID(titok_id):
                return render_template('index.html', error="This is your titok idol!!! (｡•̀ᴗ-)✧", titokID=titok_id)
            else:
                return render_template('index.html', error="Couldn't find this account !!!", titokID='haha@haha@haha')

    return render_template(send, error="", titokID=titokID)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')