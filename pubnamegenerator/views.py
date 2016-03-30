from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView

from .generator import generate_pub_name


class MainView(TemplateView):
    template_name = 'index.html'


class APIView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'name': generate_pub_name()})
