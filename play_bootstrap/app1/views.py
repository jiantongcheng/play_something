# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django import forms
# from app1.models import Author, Article, Tag

# Create your views here.

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()

def bootstrap(request):
    return render(request, 'app1/bootstrap.html')

def vue(request):
    init_data = {
        'title_small':'Follow me!!!!!',
    }
    # return HttpResponse(u"欢迎光临 自强学堂!")
    # return render(request, "app1/vue.html")
    return render(request, "app1/vue.html", locals())

def django(request):
    my_list = map(str, range(16))
    if request.method == 'POST':
        my_form = AddForm(request.POST)
        if my_form.is_valid():
            a = my_form.cleaned_data['a']
            b = my_form.cleaned_data['b']
            
            return HttpResponse(str(int(a) + int(b)))
    else:
        my_form = AddForm()

    my_dict = {
        'first':1, 
        'second':'something',
        'list': my_list,
        'num': '5',
        'form': my_form,
        }

    print locals()
    return render(request, "app1/django.html", locals())

def tt_url(request, a, b):
    return HttpResponse('Hello Wolf!')

def get_test(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET.get('c', 1)
    a = int(a)
    b = int(b)
    c = int(c)

    return HttpResponse(str(a+b+c))