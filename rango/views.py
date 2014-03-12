from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello World <a href='/rango/about'>About</a>")

def about(request):
  return HttpResponse("About page <a href='/rango'>Index</a>")
