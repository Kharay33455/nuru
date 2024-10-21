from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import smtplib
from django.core.mail import send_mail
from datetime import datetime
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
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
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip:
        ip = ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    try:
        user = User.objects.get(username = ip)
    except(User.DoesNotExist):
        user = User.objects.create(username = ip)
    if request.method == 'POST':
        title = request.POST['title']
        message = request.POST['message']
        email = request.POST['email']
        new_message = Message.objects.create(title = title, message = message, email =  email)
        new_message.save()
        msg = 'Your message was sent successfully. Someone would get back to you as soon as possible.'
        addresses = Address.objects.all()
        services = Service.objects.all()
        try:
            mosque = Mosque.objects.get(user = user)
        except(KeyError, Mosque.DoesNotExist):
            mosque = Mosque.objects.create(user = user)
            mosque.save()
        mosque.from_zoom = False
        mosque.save()

        context = {'msg': msg, 'addresses':addresses, 'services':services, 'mosque': mosque}
        return render(request, 'base/message.html', context)
    else:
        addresses = Address.objects.all()
        services = Service.objects.all()
        try:
            mosque = Mosque.objects.get(user = user)
        except(KeyError, Mosque.DoesNotExist):
            mosque = Mosque.objects.create(user = user)
            mosque.save()
        
        mosque.from_zoom = False
        mosque.save()
    

        context ={'addresses':addresses, 'services':services, 'mosque': mosque}
        return render(request, 'base/message.html', context)


    
def zoom(request, zoomie):
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip:
        ip = ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    try:
        user = User.objects.get(username = ip)
    except(User.DoesNotExist):
        user = User.objects.create(username = ip)

    try:
        mosque = Mosque.objects.get(user = user)
    except(KeyError, Mosque.DoesNotExist):
        mosque = Mosque.objects.create(user = user)
        mosque.save()
        
    if zoomie == "plus" and mosque.zoom<20:
        mosque.zoom = mosque.zoom + 0.5
        mosque.from_zoom = True
        mosque.save()
        addresses = Address.objects.all()
        services = Service.objects.all()
        context ={'addresses':addresses, 'services':services, 'mosque': mosque}
        return render(request, 'base/message.html', context)
  
   
    if zoomie =="minus" and mosque.zoom >1:
        mosque.zoom= mosque.zoom - 0.5
        mosque.from_zoom = True
        mosque.save()
        addresses = Address.objects.all()
        services = Service.objects.all()
        context ={'addresses':addresses, 'services':services, 'mosque': mosque}
        return render(request, 'base/message.html', context)
    else:
        err="MINIMUM/MAXIMUM ZOOM ACHIEVED"
        addresses = Address.objects.all()
        services = Service.objects.all()
        mosque = Mosque.objects.get(user = request.user)
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
    files = Download.objects.all()

    context = {'addresses':addresses, 'services':services,'name':mosque_name, 'files':files}
    return render(request, 'base/downloads.html', context)



def download_file(request, document_id):
    document = get_object_or_404(Download, id=document_id)
    response = HttpResponse(document.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
    return response



def suscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        emails = Email.objects.all()
        for e in emails:

            if email == e.email:
                err = 'Already suscribed'
                prayer_times = PrayerTime.objects.all()
                events = Event.objects.order_by('start')
                main = events.first()
                events = events.exclude(id = main.id)
                events = events[:3]
                addresses = Address.objects.all()
                services = Service.objects.all()
                photos = Photo.objects.all().order_by('?')
                num = len(photos)
                context = {'err':err,'prayer_time':prayer_times, 'events':events, 'main':main, 'addresses':addresses, 'services':services, 'photos':photos, 'num':num}
                return render(request, 'base/index.html', context)
            
        Email.objects.create(email = email)
        prayer_times = PrayerTime.objects.all()
        events = Event.objects.order_by('start')
        main = events.first()
        events = events.exclude(id = main.id)
        events = events[:3]
        addresses = Address.objects.all()
        services = Service.objects.all()
        photos = Photo.objects.all().order_by('?')
        num = len(photos)
        msg = 'Suscribed'

        context = {'msg':msg,'prayer_time':prayer_times, 'events':events, 'main':main, 'addresses':addresses, 'services':services, 'photos':photos, 'num':num}
        return render(request, 'base/index.html', context)


def prayers(request):
    addresses = Address.objects.all()
    services = Service.objects.all()
    
    context = {'addresses':addresses, 'services':services}
    return render(request, 'base/prayers.html', context)

def donate(request):
    addresses = Address.objects.all()
    services = Service.objects.all()
    accs = BankAccount.objects.all()
    
    context = {'addresses':addresses, 'services':services, 'accs':accs}
    return render(request, 'base/donate.html', context)

def update_mosque(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip:
        ip = ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    try:
        user = User.objects.get(username = ip)
    except(User.DoesNotExist):
        user = User.objects.create(username = ip)
    mosque_id = request.POST['mosques']
    mosque_obj = Mosque.objects.get(user = user)
    choice = Address.objects.get(id = mosque_id)
    mosque_obj.mosque = choice
    mosque_obj.from_zoom = True
    mosque_obj.save()

    addresses = Address.objects.all()
    services = Service.objects.all()
    context ={'addresses':addresses, 'services':services, 'mosque': mosque_obj}
    return render(request, 'base/message.html', context)

# views.py or any appropriate location in your Django app



def send_email(subject, from_email, mail_adds):
    subject = subject
    from_email = from_email
    to_email = mail_adds
    
    # Prepare the plain text and HTML content
    text_content = 'This is an important message.'
    html_content = render_to_string('base/email.html', {'context_variable': 'value'})

    # Create the email
    for mails in mail_adds:
        email = EmailMultiAlternatives(subject, text_content, from_email, [mails])
        email.attach_alternative(html_content, "text/html")
    
    # Send the email
        email.send()


def mailer(request):
    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == 'POST':
            subject = request.POST['subject']
            message =  request.POST['body']
            emails = Email.objects.all()
            mail_adds = []
            for email in emails:
                mail_adds.append(email)

                try:
                    send_mail(subject=subject, from_email='hello@allahunurualanuru.com', mail_adds = mail_adds)

#                    send_mail(
 #                       subject,
  #                      message,
   #                     "hello@allahunurualanuru.com",
    #                    [f'{email}'],
     #                   fail_silently=False
      #              )
                except Exception as e:
                    MailError.objects.create(email = email, error = e)
                    print(datetime.now())
            context = {'msg':'DONE'}
            return render(request, 'base/mailer.html', context)

        else:

            context = {}
            return render(request, 'base/mailer.html', context)
    else:
        return HttpResponseRedirect('/admin/')