from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        #criando um serializer pequeno para otimizar a pesquisa
        fields = ('id', 'usuario', 'comentario','nota','data')