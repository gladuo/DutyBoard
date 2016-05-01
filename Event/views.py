from django.shortcuts import render


def index(request):
    context = {

    }
    return render(request, 'DutyBoard/index.html', context=context)
