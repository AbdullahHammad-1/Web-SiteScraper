from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
# Create your views here.


def scrape(request):
    if request.method == 'POST':
        site = request.POST.get('site', '')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')


        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(name=link_text, address=link_address)

    data = Link.objects.all()

    return render(request, 'result.html', {'data': data})