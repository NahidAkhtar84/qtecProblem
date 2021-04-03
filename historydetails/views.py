from django.db.models import Count
from django.shortcuts import render
from django.views import View
from searchhistory.models import searchhistory
from users.models import User
from datetime import date


class historyDetails(View):
    def get(self, request):
        historydetails = searchhistory.objects.all().order_by('-searchtime')
        users = User.objects.all()
        keywords = searchhistory.objects.values_list('searchkey', flat=True).distinct()
        titles = searchhistory.objects.values_list('historytitle', flat=True).distinct()
        links = searchhistory.objects.values_list('historylink', flat=True).distinct()
        d3 = date.today()
        today = d3.strftime("%m/%d/%y")

        context = {
            'historydetails': historydetails,
            'users': users,
            'keywords': keywords,
            'titles': titles,
            'links': links,
            'today': today,
        }
        template = 'historydetails.html'
        return render(request, template, context)
