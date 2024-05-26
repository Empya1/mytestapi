from flask import Flask, jsonify, request

app = Flask(__name__)

app.config["SECRET_KEY"]="ဍဏဏဗမဘထတဘထဘဏဏတ"

@app.route("/")

def index():
	return jsonify({"API":"TEST API"})
	
@app.route("/login", methods=["POST"])

def login():
	
	x = request.json()
	return jsonify(x)
	
	
#app.run()
