#coding: utf-8
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy

from rest_framework import viewsets, serializers
from .models import CustomUser
from .forms import CustomUserForm

from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

# rest_framework
class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        
        # which can get, post
        fields = ('username', 'description', 'scope', 'is_active')
        
class CustomUserViewsets(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer



class UserDetailView(DetailView):
    model = get_user_model()
    #model = CustomUser
    slug_field = "username"
    template_name = "UserProfile/user_detail.html"
    
    def get_object(self, queryset=None):
        print '-----------------------------'
        print 'Start searching user from the url(flug)...'
        user = super(UserDetailView, self).get_object(queryset)
        print 'Current user is',user, '.'
        User.objects.get(username=user)
        print 'Success!'
        print '-----------------------------'
        return user
    
class UserCreateView(CreateView):
    template_name = "UserProfile/customuser_create_form.html"
    model = CustomUser
    form_class = CustomUserForm

    def form_invalid(self, form):
        return HttpResponse("form is invalid.. this is just an HttpResponse object")
        
    def get_success_url(self):
        return reverse("User:profile", kwargs={"slug": self.username})
    
    def form_valid(self, form):
        f = form.save(commit=False)
        from django.contrib.auth.hashers import make_password
        f.password = make_password(f.password)
        f.save()
        return super(UserCreateView, self).form_valid(form)

class UserUpdateView(UpdateView):
    template_name_suffix = "_update_form"
    model = CustomUser
    slug_field = "username"
    success_url = reverse_lazy("home")
    fields = ['description', 'scope']