from django.http import JsonResponse
from .models import AllChars, Episodes


data = {
        'result': '',
        'error': '',
}


def index(request):

    data = {
            'name': request.user.username,
            'url': 'slavaorlov1980.pythonanywhere.com',
            'skills': ['Python', 'Django'],
    }

    return JsonResponse(data)


def most_popular(request, status=None, gender=None, species=None):
    if status:
        query_set = AllChars.objects.filter(status=status)
    elif gender:
        query_set = AllChars.objects.filter(gender=gender)
    elif species:
        query_set = AllChars.objects.filter(species=species)
    else:
        query_set = AllChars.objects.all()


    max_count = 0
    for i in query_set:
        a = i.episodes_set.all()
        if a.count() > max_count:
            max_count = a.count()
            most_popular_char = i.name
    data['result'] = most_popular_char

    return JsonResponse(data)

def most_popular_dead(request):
    return most_popular(request, status='Dead')

def most_popular_female(request):
    return most_popular(request, gender='Female')

def most_popular_alien(request):
    return most_popular(request, species='Alien')

def all_episodes(request, id):
    char = AllChars.objects.get(pk=id)
    print(char.episodes_set.all())
    episode_list = sorted([i.id for i in char.episodes_set.all()])
    data['result'] = {'name': char.name, 'episodes list': episode_list}
    return JsonResponse(data)
