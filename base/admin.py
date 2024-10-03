from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group


class EmailAdmin(admin.ModelAdmin):
    readonly_fields = ('email',)

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj = None):
        return False
    
class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'title', 'message',)

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj = None):
        return False



admin.site.register(PrayerTime)
admin.site.register(Event)
admin.site.register(Address)
admin.site.register(Service)
admin.site.register(Photo)
admin.site.register(Message, MessageAdmin)
admin.site.register(MosqueName)
admin.site.register(Leader)
admin.site.register(Download)
admin.site.register(Email, EmailAdmin)
admin.site.register(BankAccount)
admin.site.unregister(User)
admin.site.unregister(Group)
# Register your models here.
