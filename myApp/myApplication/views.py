from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request,'myfolder/index.html')

# Create your views here.
def about(request):
    return render(request, 'myfolder/about.html')