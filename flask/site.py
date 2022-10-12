from flask import Flask, render_template, jsonify, request
app = Flask(__name__) 		

@app.route("/", methods=['GET']) 		
def hello_request():
    data = request.args.get('data')			
    return jsonify(data + "sd")

@app.route("/home")
def home():
  return "erer"

if __name__ == "__main__":
    app.run(debug=True)