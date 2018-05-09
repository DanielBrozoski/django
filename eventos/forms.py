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