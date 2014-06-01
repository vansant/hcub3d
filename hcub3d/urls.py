from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hcub3d.views

urlpatterns = patterns('',
    url(r'^$', hcub3d.views.home, name="hcub3d_home"),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
