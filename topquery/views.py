#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from database.models import Hospital
# Create your views here.
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        all_hospital = Hospital.objects.all()
        hospital = Hospital.objects.filter(hos_name__icontains=q)
        return render_to_response('search_result.html',
            {'all_hospital': all_hospital, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

def search_form(request):
    return render_to_response('search.html')