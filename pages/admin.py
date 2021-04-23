from django.contrib import admin

from .models import Page

# Customize the admin area for Pages
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('title',)
    search_fields = ('title',)


# Register your models here.
admin.site.register(Page, PageAdmin)

