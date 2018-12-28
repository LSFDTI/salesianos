from django.db import models
import math
from django.db.models import signals


class Documento(models.Model):
	rg = models.CharField(max_length=9,verbose_name='RG')
	emissor = models.CharField(max_length=6)
	dataexp = models.DateField(auto_now=False, verbose_name='Data de Expedição')
	uf = models.CharField(max_length = 2)
	cpf = models.CharField(max_length=11,verbose_name='CPF')


class Dados_base(models.Model):
	nome = models.CharField(max_length=100)
	data = models.CharField(max_length=100, verbose_name='Data de Nasciemnto')
	naturalidade = models.CharField(max_length=100, verbose_name='Naturalidade')
	uf_nat = models.CharField(max_length = 2, verbose_name='UF')
	nome_pai = models.CharField(max_length=100)
	nome_mae = models.CharField(max_length=100)
	telefone = models.CharField(max_length=100)
	local_perpetua = models.CharField(max_length=100, verbose_name='Local da Profissão Religiosa')
	data_perpetua = models.CharField(max_length=100, verbose_name='Data da Profissão Religiosa')
	local_diac = models.CharField(max_length=100, verbose_name='Local da Profissão Diaconal')
	data_diac = models.CharField(max_length=100, verbose_name='Data da Profissão Diaconal')
	local_presb = models.CharField(max_length=100, verbose_name='Local da Profissão Presbiteral')
	data_presb = models.CharField(max_length=100, verbose_name='Data da Profissão Presbiteral')
	formacao = models.CharField(max_length=100, verbose_name='Data da Profissão Presbiteral')




	
