
from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    'pubnamegenerator.views',
    url(r'^$', views.MainView.as_view(), name='main'),
    url(r'^api/pub$', views.APIView.as_view(), name='api'),
)
