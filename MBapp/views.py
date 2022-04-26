from django.shortcuts import render
from django.http import HttpResponse
from MBapp.models import Posts
from django.views.generic import ListView


class index(ListView):
    model = Posts
    template_name = "home.html"
    context_object_name = "all_list"

