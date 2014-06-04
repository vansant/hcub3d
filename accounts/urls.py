from django.conf.urls import patterns, include, url
import accounts.views

urlpatterns = patterns('accounts.views',
    url(r'^login/$', 'account_login', name='account_login'),
    url(r'^logout/$', 'account_logout', name='account_logout'),
    url(r'^profile/$', 'account_profile', name='account_profile'),
    url(r'^register/$', 'account_register', name='account_register'),
    url(r'^register/success$', 'account_register_success', name='account_register_success'),
)
