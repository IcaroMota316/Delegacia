from django.urls import path
from . import views
from . import auth_views
from django.contrib.auth import views as django_auth_views



urlpatterns = [
    # Policial
    path('policiais/', views.listar_policiais, name='listar_policiais'),
    path('policial/novo/', views.criar_policial, name='criar_policial'),
    path('policial/<int:id>/editar/', views.editar_policial, name='editar_policial'),
    path('policial/<int:id>/excluir/', views.excluir_policial, name='excluir_policial'),

    # Ocorrência
    path('ocorrencias/', views.listar_ocorrencias, name='listar_ocorrencias'),
    path('ocorrencias/criar/', views.criar, name='criar'),
    path('ocorrencias/editar/<int:id>/', views.editar_ocorrencia, name='ocorrencia_editar'),
    path('ocorrencias/excluir/<int:id>/', views.excluir_ocorrencia, name='ocorrencia_excluir'),
    
        # Vítima
    path('vitimas/', views.listar_vitimas, name='listar_vitimas'),
    path('vitima/novo/', views.criar_vitima, name='criar_vitima'),
    path('vitima/<int:id>/editar/', views.editar_vitima, name='editar_vitima'),
    path('vitima/<int:id>/excluir/', views.excluir_vitima, name='excluir_vitima'),

    # Suspeito
    path('suspeitos/', views.listar_suspeitos, name='listar_suspeitos'),
    path('suspeito/novo/', views.criar_suspeito, name='criar_suspeito'),
    path('suspeito/<int:id>/editar/', views.editar_suspeito, name='editar_suspeito'),
    path('suspeito/<int:id>/excluir/', views.excluir_suspeito, name='excluir_suspeito'),

    # Evidência
    path('evidencias/', views.listar_evidencias, name='listar_evidencias'),
    path('evidencia/novo/', views.criar_evidencia, name='criar_evidencia'),
    path('evidencia/<int:id>/editar/', views.editar_evidencia, name='editar_evidencia'),
    path('evidencia/<int:id>/excluir/', views.excluir_evidencia, name='excluir_evidencia'),
    
    
    # Autenticação
    path('', views.home, name='home'),
    path('login/', auth_views.login_usuario, name='login_usuario'),
    path('logout/', django_auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registrar/', auth_views.registrar_usuario, name='registrar_usuario'),
]
