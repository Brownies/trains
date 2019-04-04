import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.template import loader
from django.contrib.auth.decorators import login_required

from .models import Train


# @login_required(login_url="login")
def display_trains(request):
    train_list = Train.objects.all()
    print(len(train_list))
    template = loader.get_template('train_data/trains.html')
    context = {'train_list': train_list}
    return HttpResponse(template.render(context, request))


def insert_train(request, train_id):
    if request.methold != 'PUT':
        return HttpResponseBadRequest("Invalid request method")
    elif request.content_type != 'application/json':
        return HttpResponseBadRequest("Request content type is not application/json")


def index(request):
    if not request.user.is_authenticated:
        template = loader.get_template('train_data/login_or_register.html')
        return HttpResponse(template.render({}, request))

    template = loader.get_template('train_data/index.html')
    return HttpResponse(template.render({}, request))


def register(request):
    if request.method == 'GET':
        template = loader.get_template('train_data/register.html')
        return HttpResponse(template.render({}, request))

    elif request.method == 'POST':
        pass

    else:
        return HttpResponseBadRequest()
