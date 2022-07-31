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

def json2db_episodes():

    with open('ram/rnm_char_data.json') as file:
        data = json.load(file)
    
    #creating episodes dictionary
    ep_dict = {}
    for i in data:
        for e in i.get('episode'):
            ep_id = int(e.split('/')[-1])
            if not ep_dict.get(ep_id):
                ep_dict[ep_id] = e

    # create table episodes
    for i in ep_dict:
        ep = Episodes(i, ep_dict.get(i))
        ep.save()

def char_episode_link():
    with open('ram/rnm_char_data.json') as file:
        data = json.load(file)

    for i in data:
        a = AllChars.objects.get(pk=i.get('id'))
        for e in Episodes.objects.all():
            if e.episode in i.get('episode'):
                e.chars.add(a)
