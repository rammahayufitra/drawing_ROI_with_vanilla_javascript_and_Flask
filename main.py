from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        jsonData = request.get_json()
    

        json_object = json.dumps(jsonData, indent=1)
 
        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
        
        return {
            'response' : 'I am the response'
        }
    return render_template('index.html')

app.run()