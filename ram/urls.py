from django.urls import path

from . import views

urlpatterns = [
        path('', views.index),
        path('most_popular/', views.most_popular),
        path('most_popular_dead/', views.most_popular_dead),
        path('most_popular_female/', views.most_popular_female),
        path('most_popular_alien/', views.most_popular_alien),
        path('all_episodes/<id>', views.all_episodes),
]
