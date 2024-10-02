from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    prayer_times = PrayerTime.objects.all()
    events = Event.objects.order_by('start')
    main = events.first()
    events = events.exclude(id = main.id)
    events = events[:3]
    addresses = Address.objects.all()
    services = Service.objects.all()
    photos = Photo.objects.all().order_by('?')
    num = len(photos)
    context = {'prayer_time':prayer_times, 'events':events, 'main':main, 'addresses':addresses, 'services':services, 'photos':photos, 'num':num}
    return render(request, 'base/index.html', context)


def gallery(request):
    addresses = Address.objects.all()
    services = Service.objects.all()
    photos = Photo.objects.all().order_by('?')
    first = photos.first()
    context = {'addresses':addresses, 'services':services, 'photos':photos, 'first': first}
    return render(request, 'base/gallery.html', context)

def message(request):
    if request.method == 'POST':
        title = request.POST['title']
        message = request.POST['message']
        email = request.POST['email']
        new_message = Message.objects.create(title = title, message = message, email =  email)
        new_message.save()
        msg = 'Your message was sent successfully. Someone would get back to you as soon as possible.'
        addresses = Address.objects.all()
        services = Service.objects.all()
        mosque = Mosque.objects.first()
        mosque.from_zoom = False
        mosque.save()

        context = {'msg': msg, 'addresses':addresses, 'services':services, 'mosque': mosque}
        return render(request, 'base/message.html', context)
    else:
        addresses = Address.objects.all()
        services = Service.objects.all()
        mosque = Mosque.objects.first()
    

        context ={'addresses':addresses, 'services':services, 'mosque': mosque}
        return render(request, 'base/message.html', context)
    
def zoom(request, zoomie):
    mosque = Mosque.objects.first()
    if zoomie == "plus" and mosque.zoom<20:
        mosque.zoom = mosque.zoom + 0.5
        mosque.from_zoom = True
        mosque.save()
        return HttpResponseRedirect(reverse('nuru:contact'))
  
   
    if zoomie =="minus" and mosque.zoom >1:
        mosque.zoom= mosque.zoom - 0.5
        mosque.from_zoom = True
        mosque.save()
        return HttpResponseRedirect(reverse('nuru:contact'))
    else:
        err="MINIMUM/MAXIMUM ZOOM ACHIEVED"
        addresses = Address.objects.all()
        services = Service.objects.all()
        mosque = Mosque.objects.first()
        mosque.from_zoom = False
        mosque.save()

        context ={'addresses':addresses, 'services':services, 'mosque': mosque, 'err':err}
        return render(request, 'base/message.html', context)


def events(request):
    addresses = Address.objects.all()
    services = Service.objects.all()
    events = Event.objects.order_by('start')
    main = events.first()
    events = events.exclude(id = main.id)
        
    context = {'addresses':addresses, 'services':services, 'main':main, 'events':events}
    return render(request, 'base/events.html', context)

def event(request, event):
    addresses = Address.objects.all()
    services = Service.objects.all()
    event = Event.objects.get(slugger = event)

    context = {'addresses':addresses, 'services':services, 'event':event}
    return render(request, 'base/event.html', context)

def about(request):
    mosque_name = MosqueName.objects.first()
    addresses = Address.objects.all()
    services = Service.objects.all()
    leaders = Leader.objects.all().order_by('?')

    context = {'addresses':addresses, 'services':services,'name':mosque_name, 'leaders':leaders}
    return render(request, 'base/about.html', context)

def downloads(request):
    mosque_name = MosqueName.objects.first()
    addresses = Address.objects.all()
    services = Service.objects.all()

    context = {'addresses':addresses, 'services':services,'name':mosque_name}
    return render(request, 'base/downloads.html', context)

"""
def suscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        Email.objects.create(email = email)
        return render(request, 'base/index.html')
"""

