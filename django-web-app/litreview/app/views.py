from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def registration(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def flux(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def subscriptions(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def create_ticket(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def create_review(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def post(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def to_modify_review(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def to_modify_ticket(request):
    return HttpResponse('<h1>Hello Django!</h1>')