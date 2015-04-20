#coding: utf-8
from django.http import HttpRequest, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse, reverse_lazy
from django.template import RequestContext

from rest_framework import viewsets, serializers
from .models import CustomUser
from .forms import CustomUserForm, ChangePasswordForm

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
        user = super(UserDetailView, self).get_object(queryset)
        User.objects.get(username=user)
        return user
    
def ChangePasswordView(request):
    if request.method == 'GET':
        form = ChangePasswordForm()
        return render_to_response('UserProfile/change_password_form.html', RequestContext(request, {'form': form,}))
    else:
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = auth.authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                user.set_password(newpassword)
                user.save()
                return render_to_response('base.html', RequestContext(request,{'changepwd_success':True}))
            else:
                return render_to_response('UserProfile/change_password_form.html', RequestContext(request, {'form': form,'oldpassword_is_wrong':True}))
        else:
            return render_to_response('UserProfile/change_password_form.html', RequestContext(request, {'form': form,}))
    
    
class UserCreateView(CreateView):
    template_name = "UserProfile/customuser_create_form.html"
    form_class = CustomUserForm

    def form_invalid(self, form):
        return HttpResponse("form is invalid.. this is just an HttpResponse object")
        
    def get_success_url(self):
        return reverse("User:login")
    
    def form_valid(self, form):
        f = form.save(commit=False)
        from django.contrib.auth.hashers import make_password
        f.password = make_password(f.password)
        f.save()
        return super(UserCreateView, self).form_valid(form)

class UserUpdateView(UpdateView):
    template_name_suffix = "_update_form"
    #model = get_user_model()
    model = CustomUser
    print dir(CustomUser)
    print CustomUser.get_username
    slug_field = "username"
    def get_success_url(self):
        return reverse_lazy('User:profile', kwargs={'slug': self.request.user})
    #success_url = reverse_lazy('User:profile', kwargs={'slug':self.request.username})
    fields = ['description', 'scope']