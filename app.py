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
    try:
        req = request.get_json(silent=True, force=True)
        print("📦 Request JSON:", json.dumps(req, indent=2))

        if not req or "queryResult" not in req or "parameters" not in req["queryResult"] or "city_name" not in req["queryResult"]["parameters"]:
            return make_response(json.dumps({
                "fulfillmentText": "Invalid request. Please provide a valid city name."
            }), 400)

        res = weather_handler.processRequest(req)

        res = json.dumps(res)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r

    except Exception as e:
        import traceback
        print("❌ Error:", e)
        traceback.print_exc()
        return make_response(json.dumps({
            "fulfillmentText": "Internal Server Error: Something went wrong."
        }), 500)


@app.route('/webhook', methods=['GET'])
def webhook_get():
    return "Use POST method to access this endpoint.", 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

