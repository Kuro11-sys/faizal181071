from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('turunan/', views.turunan, name='turunan'),
    path('integral/', views.integral, name='integral'),
]
