from django.urls import path

from . import views

urlpatterns = [
    path('trains/<int:train_id>/location/', views.insert_train, name='insert_train'),
    path('display_trains/', views.display_trains, name='display_trains')

]
