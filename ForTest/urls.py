from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth
from django.contrib.auth.views import logout_then_login
from .views import TestMenuView, PaginationView

urlpatterns = patterns('',
    # Examples:
    #url(r'^profiles$', HomePageView.as_view(), name='home'),
    url(r'TestMenu/$', TestMenuView.as_view(), name='TestMenu'),
    url(r'pagination/', PaginationView.as_view(), name = 'TestPagination'),
)