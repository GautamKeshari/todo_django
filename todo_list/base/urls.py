# from django.urls import path

# from . import views

# urlpatterns = [
#     path('',views.taskList, name='tasks'),
# ]

from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path("",views.talkList, name='tasks'),
]
