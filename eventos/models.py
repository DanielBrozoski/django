from django.db import models

class Evento(models.Model):
	evento_id = models.AutoField(primary_key=True)
	evento_nome = models.CharField(max_length=200)
	evento_descricao = models.TextField()
	evento_descricao_curta = models.CharField(max_length=500)
	evento_data_inicio = models.DateField()
	evento_data_termino = models.DateField()
	evento_icone = models.ImageField(upload_to='evento_icone', blank=True, null=True)
	evento_banner = models.ImageField(upload_to='evento_banner', blank=True, null=True)
	
	def __str__(self):
		return self.evento_nome

class Pessoa(models.Model):
	pessoa_id = models.AutoField(primary_key=True)
	pessoa_nome = models.CharField(max_length=300)
	pessoa_sobrenome = models.CharField(max_length=300)
	pessoa_email = models.CharField(max_length=300)
	pessoa_bio = models.TextField()
	pessoa_foto = models.ImageField(upload_to='pessoa', blank=True, null=True)
	pessoa_papel = models.ManyToManyField('eventos.PapelNoEvento')

	def __str__(self):
		return self.pessoa_nome

class Atividade(models.Model):
	atividade_id = models.AutoField(primary_key=True)
	atividade_nome = models.CharField(max_length=200)
	atividade_descricao = models.TextField()
	atividade_local = models.CharField(max_length=200)
	atividade_data = models.DateField()
	atividade_hora_inicio = models.TimeField()
	atividade_hora_termino = models.TimeField()
	atividade_tags = models.ManyToManyField('eventos.Tag', blank=True, null=True)
	atividade_pessoas = models.ManyToManyField('eventos.Pessoa', blank=True, null=True)
	atividade_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

	def __str__(self):
		return self.atividade_nome

class Tag(models.Model):
	tag = models.CharField(max_length=100)

	def __str__(self):
		return self.tag

class PapelNoEvento(models.Model):
	papel_id = models.AutoField(primary_key=True)
	papel_nome = models.CharField(max_length=300)
	
	def __str__(self):
		return self.papel_nome
