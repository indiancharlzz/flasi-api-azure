from flask import Flask, jsonify


app = Flask(__name__)

data_dict = {
    'John': 'New York',
    'Alice': 'Los Angeles',
    'Bob': 'Chicago',
    'Eva': 'San Francisco',
    'David': 'Boston',
    'Grace': 'Seattle',
    'Michael': 'Austin',
    'Olivia': 'Denver',
    'Sophia': 'Miami',
    'William': 'Dallas'
}
@app.route('/', methods=['GET'])

def get_data():
    return jsonify(data_dict)


if __name__ == '__main__':
    app.run(debug=True)

