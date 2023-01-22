from django.contrib import admin
from .models import Message
# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    raw_id_fields = ['msg_sender',]
    readonly_fields = ('created_at', 'updated_at',)

admin.site.register(Message, MessageAdmin)