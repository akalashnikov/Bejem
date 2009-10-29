from django.contrib import admin
from bejem.users.models import User

class UserAdmin(admin.ModelAdmin):
    fieldsets = ( (None, {'fields': ('login', 'email')}), )
    list_display = ('login', 'email')
    ordered = ('login')
admin.site.register(User, UserAdmin)
