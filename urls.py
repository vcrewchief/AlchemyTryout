###################################################################
###  THIS FILE HANDLES THE URLS AND CALLS APPROPRIATE FUNCTION  ###
###################################################################
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from mfc import views

urlpatterns = patterns('',
    url(r'^$', 'mfc.views.index', name = 'index'),
    url(r'^cached_alch.html', 'mfc.views.cached_alch', name = 'cached_alch'),
    url(r'^cached_stack.html', 'mfc.views.cached_stack', name = 'cached_stack'),
    url(r'^alchemy.html', 'mfc.views.alchemy', name = 'alchemy'),
    url(r'^stack.html', 'mfc.views.stack', name = 'stack'),

    url(r'^admin/', include(admin.site.urls)),
)
