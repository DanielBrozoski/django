from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.evento_list, name='evento_list'),
	url(r'^novo/$', views.evento_new, name='evento_new'),
	url(r'^(?P<pk>[0-9]+)/$', views.evento_detail, name='evento_detail'),

	#url(r'^(?P<pk_evento>[0-9]+)/atividade/(?P<pk_atividade>[0-9]+)/$', views.atividade_detail, name='atividade_detail'),
	#url(r'^(?P<pk_evento>[0-9]+)/atividade/(?P<pk_atividade>[0-9]+)/editar$', views.atividade_edit, name='atividade_edit'),
	url(r'^(?P<pk>[0-9]+)/atividade/novo/$', views.atividade_new, name='atividades'),
	
]