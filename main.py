from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/test')
def hello_world():
    return 'Hello, World!'


@app.route('/login', methods=['POST', 'GET'])
def login():
    return request.args


if __name__ == '__main__':
    app.run()
