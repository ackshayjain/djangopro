from django.conf.urls import include, url
from . import views



urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^post/$',views.testform,name='testform'),
]
