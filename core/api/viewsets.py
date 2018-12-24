from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    #queryset = PontoTuristico.objects.all()
    #queryset = PontoTuristico.objects.filter(aprovado=True)
    #para usuários autenticados
    #permission_classes = (IsAuthenticated,)
    #somente para admins
    permission_classes = (IsAdminUser,)
    #pode ver mas nao pode modificar
    #permission_classes = (IsAuthenticatedOrReadOnly,)
    # Permite o controle de acesso pelo proprio Django
    # permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    # SEARCH EM CHAVE EXTRANGEIRA
    search_fields = ('nome', 'descricao', 'endereco__linha1')
    #mudando o padrao default QUERY STRINGS do id para o nome
    lookup_field = 'nome'

    # SOBREESCREVENDO MÉTODOS
    # é importante evitar essa pratica. Podemos usar os actions personalizadas
    # Filtrando resultados(GET)
    def get_queryset(self):
        #FILTRANDO POR QUERY STRINGS
        #pegando os valores declarados na url; podem ser nulos
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        #não busca no banco neste momento
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset
        #FILTRANDO POR ELEMENTO
        #return PontoTuristico.objects.filter(aprovado=True)

    # Definindo lista de recursos propria(GET)
    #def list(self, request, *args, **kwargs):
    #    return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
    #    return Response({'teste': 123})

    # Retornando variavel ao criar(POST)
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
    #    return Response({'Hello': request.data['nome']})

    # Sobreescrevendo DELETE(DELETE)
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
    #   pass

    # Sobreescrevendo retrieve(GET/RECURSO)
    def retrieve(self, request, *args, **kwargs):
         return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)
    #    pass

    # Sobreescrevendo update(PUT)
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)
    #    pass

    # Sobreescrevendo atualizando parcialmente(PATCH)
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)
     #   pass

    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass