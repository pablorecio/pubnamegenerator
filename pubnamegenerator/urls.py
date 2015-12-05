
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'pubnamegenerator.views',
    url(r'^$', 'main', name='main'),
    url(r'^api/pub$', 'api', name='api'),
)
