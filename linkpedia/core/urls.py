from django.urls import path
from django.contrib import admin
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listar, name='listar'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('atualizar/<int:pk>/', views.atualizar, name='atualizar'),
    path('remover/<int:pk>/', views.remover, name='remover'),
]