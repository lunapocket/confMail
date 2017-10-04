from django.shortcuts import render

# Create your views here.

def blank_with_pate(request):
    return render(request, 'mktitle/blank.html', {})

