
from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.counts, name='count'),
    path('about/', views.about, name='about'),
    path('viewsfile/', views.viewsfile, name='viewsfile'),
    path('homesfile/', views.homesfile, name='homesfile'),
    
]
