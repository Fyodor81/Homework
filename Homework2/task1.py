from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Hi"

@app.route('/requirements')
def reading():

    result = ''
    with open("requirements.txt", "r") as file:
        for line in file:
            result += '<p>' + line + '</p>'
    return result
if __name__ == '__main__':
    app.run(debug=True)
