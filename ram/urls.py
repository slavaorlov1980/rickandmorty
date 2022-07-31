from django.urls import path

from . import views

urlpatterns = [
        path('', views.index),
        path('most_popular/', views.most_popular),
]
