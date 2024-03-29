from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.

@login_required
def index(request):
    return render(request, 'main/index.html')

@login_required
def about(request):
    return render(request, 'main/about.html')
