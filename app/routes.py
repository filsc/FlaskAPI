#from flask import Flask
#from flask.config import Config
from app import app
from flask import jsonify
#from flask import current_app as app



@app.route('/', methods=['GET'])
def get_api():
    return jsonify({"name":"Cassie"})

