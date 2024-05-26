from flask import Flask, jsonify, request

app = Flask(__name__)

app.config["SECRET_KEY"]="ဍဏဏဗမဘထတဘထဘဏဏတ"

@app.route("/")

def index():
	return jsonify({"API":"TEST API"})
	
@app.route("/login", methods=["POST"])

def login():
	
	try:
	
		x = request.json
		x["happy"] = "Iron man"
		x["is_json"] = request.is_json
		return jsonify(x)
		
	except Exception as e:
		return jsonify({"Error": "%s"%e})
	
	
#app.run()
