from django.conf.urls import include, url
from django.contrib import admin

from accounts.views import (login_view, register_view,logout_view)

urlpatterns = [
    # Examples:
    # url(r'^$', 'ackshay.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('year.urls',namespace='home')),
    url(r'^register/',register_view,name='register'),
    url(r'^login/',login_view,name='login'),
    url(r'^logout/',logout_view,name='logout'),


]
