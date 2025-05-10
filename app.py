from flask import Flask, request, make_response
import os, json
from weather_data import WeatherData
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# ✅ Instantiate handler globally
weather_handler = WeatherData()

@app.route('/')
def index():
    return "Web app with python flask"

#def index
@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=2))

    res = weather_handler.processRequest(req)

    res = json.dumps(res)
    print(res)

    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

