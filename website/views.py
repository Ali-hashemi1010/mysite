from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
def index_view(request):
    return render(request , 'website/index.html')

def contact_view(request):
    return HttpResponse('<h1>hello contact</h1>')

def about_view(request):
    return HttpResponse('<h1>hello about</h1>')



