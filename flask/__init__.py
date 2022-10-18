from flask import Flask, render_template, jsonify, request, Blueprint

def create_app():
  app = Flask(__name__)
  
  from .views import main_views
  app.register_blueprint(main_views.bp)

  return app

# @app.route("/", methods=['GET'])
# def hello_request():
#     data = request.args.get('data')
#     return jsonify(data + "sd")

# @app.route("/home")
# def home():
#   return "erer"

# if __name__ == "__main__":
#     app.run(debug=True)