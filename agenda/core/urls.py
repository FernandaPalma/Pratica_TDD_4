from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contatos/', views.listar_contatos, name='listar_contatos'),
    path('contatos/novo/', views.cadastrar_contato, name='cadastrar_contato'),
    path('contatos/<int:contato_id>/editar/', views.atualizar_contato, name='atualizar_contato'),
    path('contatos/<int:contato_id>/remover/', views.remover_contato, name='remover_contato'),
    path('', views.home, name='home'),
]
