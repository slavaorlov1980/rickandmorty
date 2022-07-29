import json
from ram.models import AllChars, Episodes

def json2db():

    with open('ram/rnm_char_data.json') as file:
        data = json.load(file)

    for i in data:

        char = AllChars(
                name = i.get('name'),
                status = i.get('status'),
                species = i.get('species'),
                type = i.get('type'),
                gender = i.get('gender'),
                origin = i.get('origin'),
                location = i.get('location'),
                image = i.get('image'),
                url = i.get('url'),
                created = i.get('created')
        )

        char.save()
    return AllChars.objects.filter(name='Rick')

