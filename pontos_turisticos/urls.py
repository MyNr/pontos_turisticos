from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from rest_framework.authtoken import views


router = routers.DefaultRouter()
# base_name='PontoTuristico' usado para identificar o viewset quando for filtrar
router.register(r'pontoturisticos', PontoTuristicoViewSet, base_name='PontoTuristico')
router.register(r'atracoes', AtracaoViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)
router.register(r'comentarios', ComentarioViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)

]
