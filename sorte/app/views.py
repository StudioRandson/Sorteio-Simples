from django.shortcuts import render
import random

def rand(request):
    rand = random.randint(0,100)
    return render(request, 'index.html', {'rand':rand})