from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is your Flask API running on Azure Web App Service.'

if __name__ == '__main__':
    app.run()
