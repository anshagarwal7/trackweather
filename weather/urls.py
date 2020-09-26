from django.conf.urls import url
from weather.views import index,delete_city

app_name='weather'

urlpatterns = [
    url(r'^$', index ,name='home'),
    url(r'^delete/(?P<city_name>\w+)/$', delete_city , name='delete_city'),
]
