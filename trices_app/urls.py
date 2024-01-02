from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('ser_ind/',views.ser_ind,name='ser_ind'),
    path('contact/',views.contact,name='contact'),
]
