from django.contrib import admin
from .models import GroupMember, Room
# Register your models here.

class GroupMemberInline(admin.StackedInline):
    model = GroupMember
    extra = 1
    raw_id_fields = ['user', 'room']

class RoomAdmin(admin.ModelAdmin):
    inlines = [GroupMemberInline]


admin.site.register(Room, RoomAdmin)