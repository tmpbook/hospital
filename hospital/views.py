from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import View
# Create your views here.

class HomePageView(TemplateView):
    template_name= 'base.html'
 
    def get_context_data(self, **kwargs):
        print self
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['hello'] = 'hello'
        return context
