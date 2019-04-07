import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse
from django.forms import ValidationError

from .models import Train
from .forms import UserForm


@login_required(login_url="../login/")
def display_trains(request):
    if request.method != 'GET':
        return HttpResponse("Method not allowed.", status=405)

    elif not request.is_ajax():
        train_list = Train.objects.all()
        template = loader.get_template('train_data/trains.html')
        context = {'train_list': train_list}
        return HttpResponse(template.render(context, request))

    else:
        train_list = list(Train.objects.values())
        return JsonResponse(train_list, safe=False)


@csrf_exempt
def insert_train(request, train_id):
    if request.method != 'PUT':
        return HttpResponse("Method not allowed. Use PUT", status=405)
    elif request.content_type != 'application/json':
        return HttpResponseBadRequest("Content type must be application/json")

    encoding = request.encoding
    if not encoding:
        encoding = 'utf-8'
    data = json.loads(request.body.decode(encoding))
    train = Train(
        id=train_id,
        name=data['name'],
        destination=data['destination'],
        speed=data['speed'],
        latitude=data['coordinates'][0],
        longitude=data['coordinates'][1],
        time=timezone.now()
    )
    try:
        train.save()
    except ValidationError:
        return HttpResponseBadRequest("Unable to create train. Check your json.")
    return HttpResponse("OK")


def index(request):
    if request.method != 'GET':
        return HttpResponse("Method not allowed.", status=405)
    if not request.user.is_authenticated:
        template = loader.get_template('train_data/login_or_register.html')
        return HttpResponse(template.render({}, request))

    template = loader.get_template('train_data/index.html')
    return HttpResponse(template.render({}, request))


def register(request):
    if request.method == 'GET':
        template = loader.get_template('train_data/register.html')
        context = {
            'form': UserForm(),
        }
        return HttpResponse(template.render(context, request))

    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registration successful. <a href=\"..\">return to front page</a>")
        else:
            return HttpResponse("invalid form")

    else:
        return HttpResponse("Method not allowed.", status=405)
