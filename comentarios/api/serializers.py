from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        #criando um serializer pequeno para otimizar a pesquisa
        fields = ('id', 'usuario', 'comentario','data','aprovado')