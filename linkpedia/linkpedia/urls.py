from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.listar, name='listar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('atualizar/<int:pk>/', views.atualizar, name='atualizar'),
    path('remover/<int:pk>/', views.remover, name='remover'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]