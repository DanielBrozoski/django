from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from .forms import *
from .models import *

def evento_list(request):
	evento = Evento.objects.all()
	return render(request, 'eventos/evento_list.html', {'eventos':evento})

def evento_new(request):
	if request.method == 'POST':
		form = EventoForm(request.POST)
		if form.is_valid():
			evento = form.save(commit=False)
			evento.save()
			return redirect('evento_detail', pk=evento.pk)
	else:
		form = EventoForm()
	return render(request,'eventos/evento_edit.html', {'form': form})

def evento_detail(request, pk):
	atividade = Atividade.objects.filter(atividade_evento=pk)
	evento = Evento.objects.filter(pk=pk)
	return render(request, 'eventos/evento_detail.html',{'atividades':atividade,'evento': evento})