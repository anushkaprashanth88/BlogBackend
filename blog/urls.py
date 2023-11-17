from django.urls import path,include
from . import views

urlpatterns = [
    path('add/', views.addUser,name='add'),
    path('view/', views.viewUser,name='view'),
]