from flask import Flask
app = Flask(__name__)

from faker import Faker
fake = Faker()

import csv
import requests

@app.route('/')
def index():
    return "Hi"

@app.route('/requirements/')
def reading():

    result = ''
    with open("requirements.txt", "r") as file:
        for line in file:
            result += '<p>' + line + '</p>'
    return result

@app.route('/user/<users_num>', methods=['GET'])
def generate_users(users_num):
    us_num = int(users_num)
    result = ' '
    for i in range(us_num):
        result += '<p>'+ fake.name() + ' '+ fake.email() + ' ' + '</p>'
    return result

@app.route('/mean/')
def mean():
    with open("hw.csv") as file:

        file_reader = csv.DictReader(file)

        count = 0
        height = 0
        weight = 0
        for row in file_reader:
            h1 = row[' "Height(Inches)"']
            w1 = row[' "Weight(Pounds)"']

            count += 1
            height += float(h1)
            weight += float(w1)

            mean_height1 = height/count
            mean_weight1 = weight/count
            mean_height_weight = str("Mean height is " + str(mean_height1) + ' inches. Mean weight is ' + str(mean_weight1) + ' pounds')


    return mean_height_weight


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
