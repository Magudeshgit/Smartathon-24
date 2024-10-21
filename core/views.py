from django.shortcuts import render,redirect
from django.urls import reverse

from django.http.response import HttpResponse
from .models import statements, events, registrations, hackathonreg
import os
from django.core import serializers
from pathlib import Path
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.messages import error

BASE_DIR = Path(__file__).resolve().parent.parent

def home(request):
    eventdata = events.objects.all()
    return render(request, "core/index.html", {"events":eventdata})

def hackathon(request):
    ps = statements.objects.all()
    event = events.objects.get(name = "Hackathon")
    raw_ps = serializers.serialize('json', ps)
    if request.method == 'POST':
        try:
            statement = statements.objects.get(title = request.POST.get('ps'))
            if hackathonreg.objects.filter(statement=statement).count()<statement.submissions:
                registration = hackathonreg.objects.create(
                    event = event,
                    statement = statement,
                    teamname = request.POST.get("teamname"),
                    mem1 = request.POST.get("m1n"),
                    roll1 = request.POST.get("m1r"),
                    
                    mem2 = request.POST.get("m2n"),
                    roll2 = request.POST.get("m2r"),
                    
                    mem3 = request.POST.get("m3n"),
                    roll3 = request.POST.get("m3r"),
                    
                    mem4 = request.POST.get("m4n"),
                    roll4 = request.POST.get("m4r"),
                    
                    contact = request.POST.get('contact')
                )
                statement.submitted += 1
                statement.save()
                return redirect(reverse('success', kwargs={"event": event.id, "regid": registration.id}))
        except ValidationError:
            print("error Catched")
            error(request, "One or more of the provided roll numbers has already been registered.")
            return redirect('/hackathon/#register')
        except ObjectDoesNotExist:
            print("error Catched")
            error(request, "Please select the dropdown after entering Problem Statement ID to proceed")
            return redirect('/hackathon/#register')
        else:
            error(request, "Maximum registrations reached for the selected problem "+f"'{request.POST.get('ps')}', please choose a different one.")
            return redirect('/hackathon/#register')
                
    return render(request, "core/hackathon.html", {"statements": ps, "rawps":raw_ps, "event": event})

def problemstatements(request):
    ps = statements.objects.all()
    raw_ps = serializers.serialize('json', ps)
    return render(request, "core/problemstatements.html", {"statements": ps, "rawps":raw_ps})

def download_hackathon(request):
    route = str(BASE_DIR).replace('\\', '/')
    file = open(route + '/static/documents/HACKATHON TEMPLATE [SRC].pptx', 'rb')
    response = HttpResponse(file, content_type='application/vnd.openxmlformats-officedocument.presentationml.presentation')
    response['Content-Disposition'] = f"attachment; filename=HACKATHON TEMPLATE [SRC].pptx"
    return response 


def ideapitching(request):
    event = events.objects.get(name = "Idea Pitching")
    if request.method == 'POST':
        try:            
            if registrations.objects.filter(event=event).count() < event.maxsub:
                registration = registrations.objects.create(event=event,
                                                            teamname = request.POST.get("teamname"),
                                                            mem1 = request.POST.get("m1n"),
                                                            roll1 = request.POST.get("m1r"),
                                                            
                                                            mem2 = request.POST.get("m2n"),
                                                            roll2 = request.POST.get("m2r"),
                                                            
                                                            mem3 = request.POST.get("m3n"),
                                                            roll3 = request.POST.get("m3r"),
                                                            
                                                            contact = request.POST.get('contact')
                                                            )
                return redirect(reverse('success', kwargs={"event": event.id, "regid": registration.id}))
            else:
                event.isClosed = True
                event.save()
                return redirect("registrationclosed/")
        except ValidationError:
            print("error Catched")
            error(request, "One or more of the provided roll numbers has already been registered.")
            return redirect('/ideapitching/#register')
        
    return render(request, "core/ideapitching.html", {"event":event})

def ideapitching_template(request):
    route = str(BASE_DIR).replace('\\', '/')
    file = open(route + '/static/documents/IDEA PITCHING TEMPLATE [SRC].pptx', 'rb')
    response = HttpResponse(file, content_type='application/vnd.openxmlformats-officedocument.presentationml.presentation')
    response['Content-Disposition'] = f"attachment; filename=IDEA PITCHING TEMPLATE [SRC].pptx"
    return response 

def projectpresentation(request):
    event = events.objects.get(name = "Project Presentation")
    if request.method == 'POST':
        try:            
            if registrations.objects.filter(event=event).count() < event.maxsub:
                registration = registrations.objects.create(event=event,
                                                            teamname = request.POST.get("teamname"),
                                                            mem1 = request.POST.get("m1n"),
                                                            roll1 = request.POST.get("m1r"),
                                                            
                                                            mem2 = request.POST.get("m2n"),
                                                            roll2 = request.POST.get("m2r"),
                                                            
                                                            mem3 = request.POST.get("m3n"),
                                                            roll3 = request.POST.get("m3r"),
                                                            
                                                            contact = request.POST.get('contact')
                                                            )
                return redirect(reverse('success', kwargs={"event": event.id, "regid": registration.id}))
            else:
                event.isClosed = True
                event.save()
                return redirect("registrationclosed/")
        except ValidationError:
            print("error Catched")
            error(request, "One or more of the provided roll numbers has already been registered.")
            return redirect('/ideapitching/#register')
    return render(request, "core/projectpresentation.html", {"event":event})

def success(request, event, regid):
    eve = events.objects.get(id=event)
    return render(request, "core/success.html", {"event":eve, "regid":regid})

def failed(request):
    return render(request, "core/failed.html")