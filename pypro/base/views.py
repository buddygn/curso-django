from django.shortcuts import render


def home(request):
    # raise ValueError()
    return render(request, 'base/home.html')
