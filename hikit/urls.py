from django.urls import path
from hikit import views

app_name = 'hikit'

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('editpost/', views.editpost, name='editpost'),
    path('login/', views.login, name='login'),
    path('myprofile/', views.myprofile, name='myprofile'),


]