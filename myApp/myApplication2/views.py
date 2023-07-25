from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index2(request):
    return render(request,'myfolder/index2.html')

def about2(request):
    return render(request, 'myfolder/about2.html')
