from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecosSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecosSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        #criando um serializer pequeno para otimizar a pesquisa
        fields = ('id', 'nome', 'descricao', 'aprovado', 'atracoes',
                  'avaliacoes', 'comentarios', 'endereco',
                  'descricao_completa', 'descricao_completa2'
                  )

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)