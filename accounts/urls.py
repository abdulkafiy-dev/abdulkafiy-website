from django.urls import path 
from . import views

# Authentication Routes
urlpatterns = [
    path('', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
]