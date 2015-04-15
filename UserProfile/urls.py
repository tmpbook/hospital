from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth
from django.contrib.auth.views import logout_then_login
urlpatterns = patterns('',
    # Examples:
    #url(r'^profiles$', HomePageView.as_view(), name='home'),
    url(r'login/$', "django.contrib.auth.views.login", 
        {"template_name": "UserProfile/login.html"}, name='login'),
    url(r'logout/$', "django.contrib.auth.views.logout_then_login",
        name='logout'),
)