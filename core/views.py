from django.shortcuts import render
from .models import statements, events
import json
from django.core import serializers

def home(request):
    eventdata = events.objects.all()
    return render(request, "core/index.html", {"events":eventdata})

def hackathon(request):
    ps = statements.objects.all()
    raw_ps = serializers.serialize('json', ps)
    return render(request, "core/hackathon.html", {"statements": ps, "rawps":raw_ps})