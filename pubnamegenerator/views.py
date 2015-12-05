from django.shortcuts import render
from django.http import JsonResponse

from .generator import generate_pub_name

def main(request):
    return render(request, 'index.html')

def api(request):
    return JsonResponse({'name': generate_pub_name()})
