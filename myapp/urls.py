from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('Home',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.CONTACT,name="contact"),
    path('news',views.news,name="news"),
    path('donate',views.donate,name="donate"),
    path('mission',views.mission,name="mission"),
]