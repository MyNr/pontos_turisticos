from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao


class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        #criando um serializer pequeno para otimizar a pesquisa
        fields = ('id', 'nome', 'descricao')