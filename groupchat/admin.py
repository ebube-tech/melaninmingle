from django.contrib import admin
from .models import GroupMember, Conversation
# Register your models here.

class GroupMemberInline(admin.StackedInline):
    model = GroupMember
    extra = 1
    raw_id_fields = ['user']

class ConversationAdmin(admin.ModelAdmin):
    inlines = [GroupMemberInline]


admin.site.register(Conversation, ConversationAdmin)