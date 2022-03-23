
from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('loginView', views.loginView, name='login'),
    path('registerView',views.registerView,name='register'),
    path('bloodForm',views.bloodForm,name='blood form'),

    path('logoutView',views.logoutView,name='logout')
]