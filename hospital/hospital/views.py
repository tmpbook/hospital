from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name= 'base.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['hello'] = 'hello'
        return context
