#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django import template

def menu(request):
	food1 = {'name':'番茄炒飯','price':60,'comment':'好吃','is_spicy':False}
	food2 = {'name':'小白菜','price':40,'comment':'人氣推薦','is_spicy':False}

	foods = [food1,food2]

	return render_to_response('menu.html',locals())