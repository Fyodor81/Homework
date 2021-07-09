rom flask import Flask
app = Flask(__name__)

import requests

@app.route('/')
def index():
    return "Hi"

@app.route('/space/')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    r.json()

    a = r.json()
    b = a['people']
    c = "The quantity of astronauts is " + str(len(b))
    return c

if __name__ == '__main__':
    app.run(debug=True)
