from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    def get(request):
        return HttpResponse("Hello, world. You're at the polls index.")
