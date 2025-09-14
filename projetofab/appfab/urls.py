from django.urls import path
from . import views

urlpatterns = [
    path("garagem/", views.home, name="home"),
    path("listamarca/", views.lista_marcas, name="lista_marcas"),
    path("criarmarca/", views.cria_marca, name="cria_marca"),
    path("atualizarmarca/<int:pk>/", views.atualiza_marca, name="atualiza_marca"),
    path("deletarmarca/<int:pk>/", views.deleta_marca, name="deleta_marca"),

    path("listaveic/", views.lista_veiculos, name="lista_veiculos"),
    path("criarveic/", views.cria_veiculo, name="cria_veiculo"),
    path("atualizarveic/<int:pk>/", views.atualiza_veiculo, name="atualiza_veiculo"),
    path("deletarveic/<int:pk>/", views.deleta_veiculo, name="deleta_veiculo"),

    path("buscar/", views.buscar_modelos, name="buscar_modelos"),
]
