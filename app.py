from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

#Load the data from the Data Folder in JSON Format

'Link of the Data from the GITHUB Data Folder'

raw_file_url = 'https://raw.githubusercontent.com/indiancharlzz/flasi-api-azure/main/data/Data_file.json'

def load_data():

    #Send an HTTP GET request to the URL
    response = requests.get(raw_file_url)

    #Check if the request was successful(status code 200)

    if response.status_code == 200:
        try:
            #Parse the JSON data directly
            json_data = response.json()
            return json_data

        except json.JSONDecodeError:

            return {"error":"Failed to Parse the JSON response. Please check if response is received successfully."}


#API EndPoint to Retriecve the data

@app.route('', methods=['GET'])

#def get_data():
    #try:
        #data = load_data()

        #return jsonify({'data': data}), 200

    #except FileNotFoundError:

        #return jsonify({'error': 'Data File not Found'}), 404

    #except Exception as e:
       #return jsonify({'error' : str(e)}), 500

def get_data():
    data = load_data()

    if "error" in data:
        return jsonify(data), 500
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)

