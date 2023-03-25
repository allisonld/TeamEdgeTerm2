from flask import Flask, render_template
import requests



app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get("https://taylorswiftapi.onrender.com/get")
    json_data = response.json()
    return render_template('index.html', quote = json_data['quote'], song = json_data['song'], album = json_data['album'])



app.run()