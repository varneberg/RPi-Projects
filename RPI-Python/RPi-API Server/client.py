import requests
import json

API_URL = 'http://192.168.4.155:5000/data'



def POST_data(data):

	req = requests.post(API_URL, json=data)


def GET_data():
	req = requests.get(API_URL)
	print(req.text)


def create_file(fp):
	f = open(fp, "w+")
	f.close()


if __name__ == '__main__':
	data = {}
	data["plant"] = []
	data["plant"].append({
		'Temperature': '22',
		"Humidity": 70
	})
	json_object = json.dumps(data, indent=4)
	json_file = "sample.json"
	with open(json_file, "w") as outfile:
		outfile.write(json_object)


