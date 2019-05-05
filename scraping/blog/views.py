from django.shortcuts import render
import requests
import bs4
from .models import Title
from .serializers import IndiaTodaySerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet
import json
from django.core import serializers


url = "https://www.indiatoday.in/sports/cricket"


def scrape():
    Title.objects.all().delete()
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text,features="lxml")
    for a in soup.find_all(attrs={'class':'view-content'},):
        for x in a.find_all('a'):
            topic = x.text
            print(topic)
            Title.objects.create(Heading = topic)

def List_view(request):
    scrape()
    sample = Title.objects.all()
    return render(request,'hello.html',{'Titles': sample})

class XML_Tree(APIView):
    def get(self,request):
        sample = Title.objects.all()
        # data = serializers.serialize('json',sample)
        star = IndiaTodaySerializers(sample,many=True)
        # lists = json.dumps(data)
        # data = serializers.serialize('json',sample)
        return Response(star)


