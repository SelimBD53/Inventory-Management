from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('list_company/', views.list_company, name='list_company'),
    path('create_company/', views.create_company, name='create_company'),
    path('logout/', views.user_logout, name='logout'),
    path('pass_change/', views.pass_change, name='passchange'),
    path('pass_change2/', views.pass_change2, name='passchange2'),
    path('register/', views.register, name='register'),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
]
