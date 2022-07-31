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

def most_popular(request):
    a = AllChars.objects.get(pk=1)
    result = str(a.episodes_set.all())
    data['result'] = result
    return JsonResponse(data)

