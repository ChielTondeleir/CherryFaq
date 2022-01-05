#import json for filewriting
import json

#write

def write(key, value, databasefile):
	data = list(databasefile)
	data[f"{key}"] = value
	with open("database/"+databasefile, "w+") as fp:
		json.dump(data, fp, sort_keys=True, indent=4)
	return "ok"



#read

def read(key, databasefile):
	with open("database/"+databasefile, "r") as fp:
		data = json.load(fp)
	try:
		answer = data[key]
	except KeyError:
		answer = "KeyNotFound"
	return answer


def list(databasefile):
	with open("database/"+databasefile, "r") as fp:
		data = json.load(fp)
	return data