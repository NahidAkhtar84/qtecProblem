from django.contrib import admin
from .models import searchhistory

# Register your models here.

class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'searchkey', 'searchtime', 'historytitle', 'historylink', 'historysummary']


admin.site.register(searchhistory, SearchHistoryAdmin)
