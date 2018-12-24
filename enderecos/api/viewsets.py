from rest_framework.viewsets import ModelViewSet
from enderecos.api.serializers import EnderecosSerializer
from enderecos.models import Enderecos


class EnderecoViewSet(ModelViewSet):

    queryset = Enderecos.objects.all()
    serializer_class = EnderecosSerializer