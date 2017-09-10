from django.conf.urls import url
from . import views
from django.utils import timezone

app_name = 'TTapp'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    #Define the URL for TT_Site in view
    url(r'^TT_Siteabc/$', views.TT_Site),
   url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]