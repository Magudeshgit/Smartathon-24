from django.shortcuts import render
from django.http.response import HttpResponse
from .models import statements, events
import json
from django.core import serializers
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

def home(request):
    eventdata = events.objects.all()
    return render(request, "core/index.html", {"events":eventdata})

def hackathon(request):
    ps = statements.objects.all()
    raw_ps = serializers.serialize('json', ps)
    return render(request, "core/hackathon.html", {"statements": ps, "rawps":raw_ps})

def problemstatements(request):
    ps = statements.objects.all()
    raw_ps = serializers.serialize('json', ps)
    return render(request, "core/problemstatements.html", {"statements": ps, "rawps":raw_ps})

def download_hackathon(request):
    file = open(str(BASE_DIR)+'\core\downloads\HACKATHON TEMPLATE [SRC].pptx', 'rb')
    response = HttpResponse(file, content_type='application/vnd.openxmlformats-officedocument.presentationml.presentation')
    response['Content-Disposition'] = f"attachment; filename=HACKATHON TEMPLATE [SRC].pptx"
    return response 