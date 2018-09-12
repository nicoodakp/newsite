from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('resume', views.resume, name='resume'),
    # path('weather', views.weather, name='weather'),

]
