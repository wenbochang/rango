from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "Bold var from context"}
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {'message': "About var"}
    return render_to_response('rango/about.html', context_dict, context)
    
