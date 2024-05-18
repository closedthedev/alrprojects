from django.shortcuts import render


def index1(request):
    return render(request, 'galeria/index.html')
