from django.contrib import admin
from .models import *


@admin.register(RegTer)
class RegTerAdmin(admin.ModelAdmin):
    list_display = ['nome_municipio', 'nome_uf', 'codigo_ibge']
    ordering = ('nome_municipio', )
    fields = [
        'uf', 
        'nome_uf', 
        'regiao_geografica_intermediaria', 
        'nome_regiao_geografica_intermediaria', 
        'regiao_geografica_imediata', 
        'nome_regiao_geografica_imediata', 
        'mesorregiao_geografica', 
        'nome_mesorregiao', 
        'microrregiao_geografica', 
        'nome_microrregiao', 
        'municipio', 
        'codigo_municipio_completo', 
        'nome_municipio', 
        'codigo_ibge', 
        'repasses_f',
        'total_repassado',
        'total_descontado',
        'total_repassado_liquido']

    readonly_fields = [
        'uf', 
        'nome_uf', 
        'regiao_geografica_intermediaria', 
        'nome_regiao_geografica_intermediaria', 
        'regiao_geografica_imediata', 
        'nome_regiao_geografica_imediata', 
        'mesorregiao_geografica', 
        'nome_mesorregiao', 
        'microrregiao_geografica', 
        'nome_microrregiao', 
        'municipio', 
        'codigo_municipio_completo', 
        'nome_municipio', 
        'codigo_ibge', 
        'repasses_f',
        'total_repassado',
        'total_descontado',
        'total_repassado_liquido']


@admin.register(Repasses)
class RepassesAdmin(admin.ModelAdmin):
    list_display = ['nome_municipio', 'valor_total', 'desconto', 'valor_liquido']

    fields = [
            'codigo_ibge',
            'bloco',
            'grupo',
            'acao_detalhada',
            'competencia_parcela',
            'n_ob',
            'data_ob',
            'banco_ob',
            'agencia_ob',
            'conta_ob',
            'valor_total',
            'desconto',
            'valor_liquido',
            'observacao',
            'processo',
            'tipo',
            'n_proposta']

    readonly_fields = [
            'codigo_ibge',
            'bloco',
            'grupo',
            'acao_detalhada',
            'competencia_parcela',
            'n_ob',
            'data_ob',
            'banco_ob',
            'agencia_ob',
            'conta_ob',
            'valor_total',
            'desconto',
            'valor_liquido',
            'observacao',
            'processo',
            'tipo',
            'n_proposta']


