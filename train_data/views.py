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
    return HttpResponse("hello")
