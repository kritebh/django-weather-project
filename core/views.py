from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    try:
        query = request.GET.get('query','patna')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid=YourAPIkey&units=metric"

        response = requests.request("GET",url).json()
        speed = "{:.2f}".format(1.6*response['wind']['speed'])
        data ={
            'name':response['name'],
            'weather':response['weather'][0]['description'],
            'icon':response['weather'][0]['icon'],
            'temp':response['main']['temp'],
            'sunrise':response['sys']['sunrise'],
            'sunset':response['sys']['sunset'],
            'windspeed':speed,
        }
        return render(request,'core/index.html',context={'data':data})
    except:
        return render(request,'core/error.html',context={'data':query})