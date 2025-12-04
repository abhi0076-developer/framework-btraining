from django.urls import path
from .import views

urlpatterns=[
    path('',views.add_employee,name='home'),
    path('add/',views.add_employee,name='add_employee.html'),
    path('success/',views.success,name='success'),
]