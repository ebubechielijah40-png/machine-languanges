from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.login_view, name='login'), 
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('languages/', views.language_list, name='language_list'),
    path('languages/<int:pk>/', views.language_detail, name='language_detail'),
    path('lessons/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('lessons/<int:pk>/try/', views.try_it, name='try_it'),
    path('lessons/<int:pk>/complete/', views.lesson_complete, name='lesson_complete'),
    path('hardware/', views.hardware_list, name='hardware_list'),
    path('hardware/<slug:slug>/', views.hardware_detail, name='hardware_detail'),
    path('hardware/<slug:slug>/<int:challenge_pk>/', views.hardware_challenge, name='hardware_challenge'),
    path('hardware/<slug:slug>/<int:challenge_pk>/complete/', views.hardware_complete, name='hardware_complete'),
]
