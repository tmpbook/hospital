from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth
from django.contrib.auth.views import logout_then_login
from .views import UserDetailView
from .views import UserCreateView
from .views import UserUpdateView
from .views import ChangePasswordView
urlpatterns = patterns('',
    # Examples:
    #url(r'^profiles$', HomePageView.as_view(), name='home'),
    url(r'login/$', "django.contrib.auth.views.login", 
        {"template_name": "UserProfile/login.html"}, name='login'),
    url(r'logout/$', "django.contrib.auth.views.logout_then_login",
        name='logout'),
    url(r'profile/(?P<slug>\w+)/$', auth(UserDetailView.as_view()), name='profile'),
    url(r'register/$', UserCreateView.as_view(), name='register'),
    url(r'update/(?P<slug>\w+)/$', auth(UserUpdateView.as_view()), name='update'),
    url(r'changepwd/$',auth(ChangePasswordView), name='changepassword'),
)