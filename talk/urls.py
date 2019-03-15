from django.conf.urls import include, url
from django.contrib import admin
from talk_app.api import v1_api

admin.autodiscover()


urlpatterns = [
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
]

