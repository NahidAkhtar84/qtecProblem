from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
import requests
from bs4 import BeautifulSoup
from .models import searchhistory
from users.models import User


# Create your views here.
class Index(View):
    def get(self, request):
        username = request.session.get('customer_id')
        history = searchhistory.objects.filter(user=username).order_by('-searchtime')
        template = 'index.html'
        context = {
            'history': history,
        }
        return render(request, template, context)

    def post(self, request):
        if request.method == 'POST':
            pst = request.POST
            searchkeyword = pst.get('searchkeyword')
            user = request.session.get('customer_id')

            params = {"q": searchkeyword}
            r = requests.get("https://search.yahoo.com/search", params=params)

            soup = BeautifulSoup(r.text, "html.parser")

            results = soup.find("div", {"id": "results"})

            links = results.findAll("div", {"class": "algo"})

            for item in links:
                try:
                    item_text = item.find("a").text
                    item_href = item.find("a").attrs["href"]

                    if item_text and item_href:
                        history = searchhistory(
                            user=User(id=user),
                            searchkey=searchkeyword,
                            historytitle=item_text,
                            historylink=item_href,
                            historysummary=item.parent.find("p", {"class": "fz-ms lh-1_43x"}).text,
                        )
                        history.save()
                except:
                    print('some error occred!')

            return redirect('home')
