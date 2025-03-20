from django.shortcuts import render
import requests, datetime
import json
# Create your views here.

def home(request):
    if request.method == 'POST':
        api_key = "cb66bbbc7a441d15e85c29196a6fe0da"
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={request.POST["city"]}&appid={api_key}',verify=False)
        data = response.json()
        return render(request,'index.html',{'data':data['main'],'city':request.POST['city']})
    else:
        return render(request,'index.html')
        
