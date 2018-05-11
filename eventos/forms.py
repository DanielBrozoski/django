from django import forms
from .models import *

class EventoForm(forms.ModelForm):
	class Meta:
		model = Evento
		fields = ('evento_nome', 'evento_descricao', 'evento_descricao_curta', 'evento_data_inicio', 'evento_data_termino', 'evento_icone', 'evento_banner')
		labels = {
			'evento_nome':'Nome do Evento:',
			'evento_descricao':'Descrição:',
			'evento_descricao_curta':'Descrição breve:',
			'evento_data_inicio':'Data de Início:',
			'evento_data_termino':'Data de Término:',
			'evento_icone':'Icone do evento:',
			'evento_banner':'Banner do evento:',
		}

class AtividadeForm(forms.ModelForm):
	class Meta:
		model = Atividade
		fields = ('atividade_nome', 'atividade_descricao', 'atividade_local' ,'atividade_data', 'atividade_hora_inicio', 'atividade_hora_termino', 'atividade_tags', 'atividade_pessoas', 'atividade_evento')
		labels = {
			'atividade_nome':'Nome da Atividade:',
			'atividade_descricao':'Descrição:',
			'atividade_local':'Local:',
			'atividade_date': 'Data:',
			'atividade_hora_inicio':'Hora de Início:',
			'atividade_hora_termino':'Hora de Término:',
			'atividade_tags':'Tags:',
			'atividade_pessoas':'Responsável pela atividade:',
			'atividade_evento': 'Evento da Atividade:',
		}