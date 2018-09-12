from django.shortcuts import render


def index(request):
    return render(request, 'personal/header.html')

def about(request):
    return render(request, 'personal/about.html')

def resume(request):
    return render(request, 'personal/resume.html')

# def index(request):
#     return render(request, 'personal/weather.html')
