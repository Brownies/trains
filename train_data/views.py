import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
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
        context = {'form': UserCreationForm()}
        return HttpResponse(template.render(context, request))

    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            return HttpResponse("Registration succesful. <a href=\"..\">return to front page</a>")
        else:
            return HttpResponse("invalid form")

    else:
        return HttpResponseBadRequest()
