from rest_framework.serializers import ModelSerializer
from enderecos.models import Enderecos


class EnderecosSerializer(ModelSerializer):
    class Meta:
        model = Enderecos
        #criando um serializer pequeno para otimizar a pesquisa
        fields = ('id', 'linha1', 'cidade','estado','pais')