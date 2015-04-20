from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
class TestMenuView(TemplateView):
    template_name = "ForTest/menu.html"
    
    def get_context_data(self, **kwargs):
        context = super(TestMenuView, self).get_context_data(**kwargs)
        context['hello'] = 'hello'
        return context
    
class PaginationView(TemplateView):
    template_name = 'ForTest/pagination.html'

    def get_context_data(self, **kwargs):
        context = super(PaginationView, self).get_context_data(**kwargs)
        lines = []
        for i in range(10000):
            lines.append('Line %s' % (i + 1))
        paginator = Paginator(lines, 10)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        context['lines'] = show_lines
        return context