from django.views import View
from django.http import JsonResponse
from .models import *

from django.core.serializers import serialize

data = {
        'result': '',
        'error': '',
}


class IndexView(View):

    def get(self, request):
        data = {
                'name': request.user.username,
                'url': 'http://www.ya.ru',
                'skills': ['Python', 'Django'],
        }
        return JsonResponse(data)


class RAMView(View):
    pass
    """
    def most_popular(self):
        name = CharEpisodeLink.objects.all()
        data['result'] = name
        return JsonResponse(data) """

