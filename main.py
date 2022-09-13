from ast import parse
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        jsonData = request.get_json()
        dictionary = {str(len(jsonData["status"])):str(jsonData["area"])}
        with open('sample.json') as f:
            data = json.load(f)
        data.update(dictionary)
        with open('sample.json', 'w') as f:
            json.dump(data, f)
        return {
            'response' : 'I am the response'
        }
    return render_template('index.html')

app.run()