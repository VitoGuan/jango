from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Helllllo World!'
    return render(request, 'hello.html', context)
