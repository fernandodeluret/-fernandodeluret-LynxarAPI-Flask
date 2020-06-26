
from flask import Flask
app = Flask(__name__)
from env import env

@app.route('/')
def hello_world():
    return env['key']


if __name__ == "__main__":
    app.run()