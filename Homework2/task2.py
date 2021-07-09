from flask import Flask
from faker import Faker
fake = Faker()

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi"

@app.route('/user/<users_num>', methods=['GET'])
def generate_users(users_num):
    us_num = int(users_num)
    result = ' '
    for i in range(us_num):
        result += '<p>'+ fake.name() + ' '+ fake.email() + ' ' + '</p>'
    return result

if __name__ == '__main__':
    app.run(debug=True)