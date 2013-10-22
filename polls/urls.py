# To call the view, we need to map it to a URL - and for this we need a URLconf.
from django.conf.urls import patterns, include, url

from polls import views

# covnversion to generic views
urlpatterns = patterns('',
	#ex: /polls/
	url(r'^$', views.IndexView.as_view(), name = 'index'),
	#ex: /polls/5/
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name = 'details'),
	#ex: /polls/5/results/
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name = 'results'),
	#ex: /polls/5/vote
	url(r'^(?P<question_id>\d+)/vote/$', views.vote, name = 'vote'),
)

# The next step is to point the root URLconf at the polls.urls module. 
# In [appname]/urls.py insert an include(), leaving you with: