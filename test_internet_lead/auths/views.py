
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'auths/auths.html',)


@login_required
def home(request):
  return render(request, 'auths/home.html')