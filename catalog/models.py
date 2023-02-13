from django.db import models
from django.utils.html import format_html


class RegTer(models.Model):
    uf = models.CharField(max_length=3)
    nome_uf = models.CharField(max_length=55)
    regiao_geografica_intermediaria = models.CharField(max_length=5)
    nome_regiao_geografica_intermediaria = models.CharField(max_length=55)
    regiao_geografica_imediata = models.CharField(max_length=8)
    nome_regiao_geografica_imediata = models.CharField(max_length=55)
    mesorregiao_geografica = models.CharField(max_length=4)
    nome_mesorregiao = models.CharField(max_length=55)
    microrregiao_geografica = models.CharField(max_length=4)
    nome_microrregiao = models.CharField(max_length=55)
    municipio = models.CharField(max_length=10)
    codigo_municipio_completo = models.CharField(max_length=10)
    nome_municipio = models.CharField(max_length=55)
    codigo_ibge = models.CharField(max_length=7)

    def __str__(self) -> str:
        return self.codigo_ibge


    def repasses(self):
        return Repasses.objects.filter(codigo_ibge=self)


    @property
    def repasses_f(self):
        buf = '<table>'\
                '<thead>'\
                    '<tr>'\
                        '<th scope="col">Valor repasse</th>'\
                        '<th scope="col">Desconto</th>'\
                        '<th scope="col">Valor líquido</th>'\
                    '</tr>'\
                '</thead>'\
                '<tbody>'
        for r in self.repasses():
            buf += f'<tr>'\
                        f'<td>R$ {r.valor_total:,.2f}</td>'\
                        f'<td>R$ {r.desconto:,.2f}</td>'\
                        f'<td>R$ {r.valor_liquido:,.2f}</td>'\
                    f'</tr>'
        buf += '</tbody>'\
            '</table>'
        return format_html(buf)



    @property
    def total_repassado(self):
        soma = 0
        for r in self.repasses():
            soma += r.valor_total
        return f'R$ {soma:,.2f}'

    @property
    def total_descontado(self):
        soma = 0
        for r in self.repasses():
            soma += r.desconto
        return f'R$ {soma:,.2f}'


    @property
    def total_repassado_liquido(self):
        soma = 0
        for r in self.repasses():
            soma += r.valor_liquido
        return f'R$ {soma:,.2f}'



class Repasses(models.Model):
    codigo_ibge = models.ForeignKey('RegTer', on_delete=models.CASCADE)
    bloco = models.TextField(max_length=200)
    grupo = models.TextField(max_length=200)
    acao_detalhada = models.TextField(max_length=200)
    competencia_parcela = models.TextField(max_length=200)
    n_ob = models.TextField(max_length=200)
    data_ob = models.TextField(max_length=200)
    banco_ob = models.TextField(max_length=200)
    agencia_ob = models.TextField(max_length=200)
    conta_ob = models.TextField(max_length=200)
    valor_total = models.FloatField()
    desconto = models.FloatField()
    valor_liquido = models.FloatField()
    observacao = models.TextField(max_length=200)
    processo = models.TextField(max_length=200)
    tipo = models.TextField(max_length=200)
    n_proposta = models.TextField(max_length=200)


    @property
    def nome_municipio(self):
        return RegTer.objects.get(codigo_ibge=self.codigo_ibge).nome_municipio

