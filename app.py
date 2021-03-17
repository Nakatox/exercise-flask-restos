from flask import Flask,jsonify,request
import overpass
api = overpass.API()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api')
def api_root():
    return jsonify({"restos":"http://127.0.0.1:5000/api/restos"})

@app.route("/api/restos/<city>", methods=["GET", "PUT"])
def restos(city):
    if request.method == "GET":
        response = api.get (f"""area[name="{city}"]; node[amenity=street](area);""")
        return response
