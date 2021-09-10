import requests
import json
from pathlib import Path
from flask import Flask, request, jsonify
import os


app = Flask(__name__)


def get_ip():
	return os.popen("hostname -I | awk '{print $1}'").read()


@app.route('/')
def index():
	return get_ip()


def checkfile(file):
	open(file, 'w')


@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def data():
	json_file = "./data/data.json"
	if request.method == 'GET':
		return "hi"
	elif request.method == 'POST':
		json_data = request.get_json()
		checkfile(json_file)

		return "woow"

	else:
		return "What"


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
