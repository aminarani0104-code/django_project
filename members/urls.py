from django.urls import path
from . import views

urlpatterns = [
    path('', views.persons, name='members'),
    path('testing/', views.testing, name='testing'),
    path('persons/details/<int:id>', views.details, name='details'),
]
