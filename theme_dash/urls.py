from django.urls import path
from . import views

app_name = 'theme_dash'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('superadmin/users/', views.superadmin_users_view, name='superadmin_users'),
    path('superadmin/logs/', views.superadmin_logs_view, name='superadmin_logs'),
    path('projects/', views.projects_view, name='projects'),
    path('forms/', views.forms_view, name='forms'),
    path('tables/', views.tables_view, name='tables'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('starter/', views.starter_view, name='starter'),
]
