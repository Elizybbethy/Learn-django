#Here we are preparing to create urls to be used in our application
from django.urls import path
#lets import views file from "myApplication" Application
from myApplication import views
urlpatterns = [
    #incase request index, consider file views
    path('index/', views.index, name= 'index'),
    path('about/', views.about, name= 'about'),
]
