from django.conf.urls import patterns, include, url
from hospital.views import HomePageView
from rest_framework import routers
from UserProfile import views
from django.contrib import admin
from django.contrib.auth.decorators import login_required as auth
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewsets)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^routers/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/', include('UserProfile.urls', namespace='User')),
    # test App
    url(r'^test/', include('ForTest.urls', namespace='ForTest')), 
)