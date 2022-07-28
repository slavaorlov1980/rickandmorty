import json
from ram.models import AllChars, Episodes

def json2db():

    with open('ram/rnm_char_data.json') as file:
        data = json.load(file)

    print(data)

def allchars():
    return AllChars.objects.all()
