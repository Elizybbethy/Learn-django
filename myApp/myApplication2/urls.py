#Here we are preparing to create urls to be used in our application
from django.urls import path
#lets import views file from "myApplication" Application
from myApplication2 import views
urlpatterns = [
    #incase request index, consider file views
    path('index2/', views.index2, name= 'index2'),
    path('about2/', views.about2, name= 'about2'),
]