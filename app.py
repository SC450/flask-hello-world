from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'How many tickles does it take to make an octopus laugh? Ten-tickles!'
