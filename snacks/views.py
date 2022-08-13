from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Snack

# Create your views here.

class SnackList(ListView):
    template_name = "snack_list.html"
    model = Snack
    context_object_name = "snack_list"


class SnackDetail(DetailView):
    template_name = "snack_detail.html"
    model = Snack
    context_object_name = "detail"

class AboutView(TemplateView):
    template_name = 'about.html'