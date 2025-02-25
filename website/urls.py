from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.contact_page, name='contact_page'),
]
