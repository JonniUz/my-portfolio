from django.contrib import admin
from .models import Portfolio, Message


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'link']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_num']


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Message, MessageAdmin)
