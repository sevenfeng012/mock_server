from django.contrib import admin

from .models import API


class APIAdmin(admin.ModelAdmin):
    list_display = ('slug','name')
    fields = ('content','slug','name')

admin.site.register(API,APIAdmin)

