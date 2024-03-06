from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Hospitalapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inner-page/', views.inner, name='inner-page'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('details/', views.details, name='details'),
    path('value/', views.value, name='value'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    ]
