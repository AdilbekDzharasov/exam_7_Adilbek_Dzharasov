from django.contrib import admin

from webapp.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'text_entry', 'status']
    list_filter = ['id', 'name', 'email', 'text_entry', 'status', 'created_at']
    search_fields = ['id', 'name', 'email']
    fields = ['id', 'name', 'email', 'text_entry', 'status']
    readonly_fields = ['id']


admin.site.register(Entry, EntryAdmin)
