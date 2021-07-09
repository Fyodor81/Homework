rom flask import Flask
app = Flask(__name__)
import csv

@app.route('/')
def index():
    return "Hi"

@app.route('/mean')
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

if __name__ == '__main__':
    app.run(debug=True)
