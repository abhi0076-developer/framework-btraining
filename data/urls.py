from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    path('', views.add_student, name='add_student'),
    path('success/', views.success, name='success'),
]
