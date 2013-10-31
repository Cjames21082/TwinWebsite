from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'polls.views.home', name='home'),
     url(r'^polls/guess', 'polls.views.guess', name='guess'),

    #url(r'^twinsite/', include('twinsite.foo.urls')),
    url(r'^polls/', include('polls.urls', namespace = 'polls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
