from django.db.models import Sum
from django.db import models
from django.db.models.enums import Choices
from django import forms
import datetime
from django.utils import timezone

# Create your models here.

class Sure(models.Model):
       
    #pub_date = models.DateTimeField('date published')
   
    class sure01(models.IntegerChoices):
        Nunca = 4
        Em_1_ou_2_dias = 3
        Em_3_ou_4_dias = 2
        Em_5_ou_6_dias = 1
        Todos_os_dias = 0

    q01 = models.IntegerField(choices=sure01.choices)
    q02 = models.IntegerField(choices=sure01.choices)
    q03 = models.IntegerField(choices=sure01.choices)
    
    class sure02(models.IntegerChoices):
        Todo_o_tempo = 4
        A_maior_parte_do_tempo = 3
        Boa_parte_do_tempo = 2
        Uma_pequena_parte_do_tempo = 1
        Em_nenhum_momento = 0

    q04 = models.IntegerField(choices=sure02.choices)
    q05 = models.IntegerField(choices=sure02.choices)
    q06 = models.IntegerField(choices=sure02.choices)
    q07 = models.IntegerField(choices=sure02.choices)
    q08 = models.IntegerField(choices=sure02.choices)
    q09 = models.IntegerField(choices=sure02.choices)
    q10 = models.IntegerField(choices=sure02.choices)
    q11 = models.IntegerField(choices=sure02.choices)
    q12 = models.IntegerField(choices=sure02.choices)
    q13 = models.IntegerField(choices=sure02.choices)
    q14 = models.IntegerField(choices=sure02.choices)
    q15 = models.IntegerField(choices=sure02.choices)
    q16 = models.IntegerField(choices=sure02.choices)
    q17 = models.IntegerField(choices=sure02.choices)
    q18 = models.IntegerField(choices=sure02.choices)
    q19 = models.IntegerField(choices=sure02.choices)
    q20 = models.IntegerField(choices=sure02.choices)
    q21 = models.IntegerField(choices=sure02.choices)
    
    
    class sure03(models.IntegerChoices):
        Não_importante = 4
        Pouco_importante = 3
        Importante = 2
        Muito_Importante = 1

    q22 = models.IntegerField(choices=sure03.choices)
    q23 = models.IntegerField(choices=sure03.choices)
    q24 = models.IntegerField(choices=sure03.choices)
    q25 = models.IntegerField(choices=sure03.choices)
    q26 = models.IntegerField(choices=sure03.choices)
    

    
    
    
    
