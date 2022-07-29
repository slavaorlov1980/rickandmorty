from django.views import View
from django.http import JsonResponse
from .models import AllChars, Episodes

data = {
        'result': '',
        'error': '',
}


class IndexView(View):

    def get(self, request):
        data = {
                'name': request.user.username,
                'url': 'slavaorlov1980.pythonanywhere.com',
                'skills': ['Python', 'Django'],
        }
        return JsonResponse(data)


class RAMView(View):
    pass
    """
    def most_popular(self):

        return JsonResponse(data) """

