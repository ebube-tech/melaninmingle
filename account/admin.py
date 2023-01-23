from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm

from account.models import Account, Profile

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile
    list_display = '__all__'
    readonly_fields = ('created_at', 'updated_at')


class AccountAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    inlines = [ProfileInline]
    search_fields = ['email']


    # The fields to be used in displaying the User model.
    # These override the definitions on the base AccountAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_admin', )
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. AccountAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', )
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new AccountAdmin...
admin.site.register(Account, AccountAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)