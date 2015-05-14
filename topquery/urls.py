from django.conf.urls import patterns,url,include
urlpatterns = patterns('',
    url(r'^search_form/$','topquery.views.search_form'),
    url(r'^search/$','topquery.views.search'),
    )
    