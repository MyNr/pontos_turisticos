from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Enderecos


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    avaliacoes = models.ManyToManyField(Avaliacao)
    comentarios = models.ManyToManyField(Comentario)
    endereco = models.ForeignKey(Enderecos, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def descricao_completa2(self):
        return '%s - %s' % (self.nome, self.descricao)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Pontos Turísticos"
