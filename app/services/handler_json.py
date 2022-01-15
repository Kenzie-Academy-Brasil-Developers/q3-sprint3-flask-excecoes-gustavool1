from json import JSONDecodeError, load,dump
from flask import jsonify

FILENAME = 'database.json'

def reading_json():
    try:
        with open(f"./app/database/{FILENAME}", 'r') as archive:
            return load(archive)
            
    except (FileNotFoundError, JSONDecodeError):
        with open(f"./app/database/{FILENAME}", 'w+') as archive:
            obj = {"data":[]}
            dump(obj, archive, indent=2)
            return obj
    


def writing_json(data):
    content = reading_json()
    data_list = content["data"]
    data_list.append(data)
    print(data)
    with open(f"./app/database/{FILENAME}", 'w') as archive:
        content = dump({"data":data_list},archive, indent=2)
        return {"data":data} 
