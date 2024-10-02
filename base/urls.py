from django.urls import path
from . import views

app_name = 'nuru'

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.message, name='contact'),
    path('contact/zoom<slug:zoomie>/', views.zoom, name='zoom'),
    path('events/', views.events, name='events'),
    path('events/<slug:event>', views.event, name='event'),
    path('about-us', views.about, name='about'),
    path('downloads', views.downloads, name='downloads'),
]
