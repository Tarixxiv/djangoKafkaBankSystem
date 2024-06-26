from django.http import HttpResponse
from django.urls import path
from . import views


def okay(request):
    return HttpResponse('pretend-binary-data-here', content_type='image/jpeg')


urlpatterns = [
    path('', views.home, name='home'),
    path('favicon.ico', okay)

]
