from itertools import count
from multiprocessing.sharedctypes import Value
from django import db
from django.shortcuts import redirect, render
from app.forms import SureForm
from app.models import Sure
from django.http import HttpResponse
from django.template import loader
from django.db.models import Avg, Sum, Count
import random

from django.http import JsonResponse
import json
# Create your views here.

def home(request):
    data = {}
    data['db'] = Sure.objects.all()
    return render(request, 'index.html', data)

def dashboard(request):
    data = Sure.objects.all()
    return render(request, 'dashboard.html', data)

def dash(request):
  mydata = Sure.objects.all()
  template = loader.get_template('dash.html')
  context = {
    'mydata': mydata,
  }
  return HttpResponse(template.render(context, request))

def dash2(request):
    template = loader.get_template('dash2.html')
    tam = Sure.objects.count()
    #listas para interações
    lista = ['q01','q02','q03','q04','q05','q06','q07','q08','q09','q10', 'q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21','q22','q23','q24','q25','q26']
    lista_beber = ['q01','q02','q03','q04','q05','q06']
    lista_cuidados = ['q07','q08','q09','q10', 'q11']
    lista_relacionamentos = ['q12','q13','q14','q15']
    lista_recursos = ['q16','q17','q18']
    lista_perspectiva = ['q19','q20','q21']
    
    #soma de todas as pontuações e media geral
    lista_soma = []
    
    for x in lista:
        somaq = Sure.objects.values_list(x, flat=True)
        lista_soma.append(sum(somaq))
    
    media_total = int(sum(lista_soma)/(tam))
    valor_minimo = random.randint((media_total-14),(media_total-5))
    valor_maximo = random.randint((media_total+5),(media_total+14))
    
    #soma por setor
    #listas para somar
    lista_beber_soma = []
    lista_cuidados_soma = []
    lista_relacionamentos_soma = []
    lista_recursos_soma = []
    lista_perspectiva_soma = []
    
    for x in lista_beber:
        somaq = Sure.objects.values_list(x, flat=True)
        lista_beber_soma.append(sum(somaq))
    somat_beber = sum(lista_beber_soma)

    for x in lista_cuidados:
        somaq = Sure.objects.values_list(x, flat=True)
        lista_cuidados_soma.append(sum(somaq))
    somat_cuidados = sum(lista_cuidados_soma)

    for x in lista_relacionamentos:
        somaq = Sure.objects.values_list(x, flat=True)
        lista_relacionamentos_soma.append(sum(somaq))
    somat_relacionamentos = sum(lista_relacionamentos_soma)
    
    for x in lista_recursos:
        somaq = Sure.objects.values_list(x, flat=True)
        lista_recursos_soma.append(sum(somaq))
    somat_recursos = sum(lista_recursos_soma)
    
    for x in lista_perspectiva:
        somaq = Sure.objects.values_list(x, flat=True)
        lista_perspectiva_soma.append(sum(somaq))
    somat_perspectiva = sum(lista_perspectiva_soma)
    
    context = {
    'tam': tam,
    'lista': lista,
    'lista_soma': lista_soma,
    'media_total': media_total,
    'valor_minimo': valor_minimo,
    'valor_maximo': valor_maximo,
    'somat_beber': somat_beber,
    'somat_cuidados': somat_cuidados,
    'somat_relacionamentos': somat_relacionamentos,
    'somat_recursos': somat_recursos,
    'somat_perspectiva': somat_perspectiva,
    
  }
    return HttpResponse(template.render(context, request))

def form(request):
    data = {}
    data['form'] = SureForm()
    return render(request,'form.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Sure.objects.get(pk=pk)
    data['form'] = SureForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Sure.objects.get(pk=pk)
    form = SureForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def delete(request, pk):
    db = Sure.objects.get(pk=pk)
    db.delete()
    return redirect('home')
    
def create(request):
    form = SureForm(request.POST or None) 
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request, pk):
    data = {}
    data['db'] = Sure.objects.get(pk=pk)
    return render(request, 'view.html', data)

def json(request):
    data = list(Sure.objects.values())
    return JsonResponse(data, safe=False)



