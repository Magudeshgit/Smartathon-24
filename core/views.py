from django.shortcuts import render
from .models import statements
import json
from django.core import serializers

def home(request):
    return render(request, "core/index.html")

def hackathon(request):
    ps = statements.objects.all()
    raw_ps = serializers.serialize('json', ps)
    return render(request, "core/hackathon.html", {"statements": ps, "rawps":raw_ps})