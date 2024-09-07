from django.shortcuts import render,redirect
import requests
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a2eaa2ca76d883f4c97505a5afc751f7'
    

    err_msg = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        # print(request.POST)
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city = City.objects.filter(name=new_city).count()

            if existing_city == 0:
                r = requests.get(url.format(new_city)).json()

                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg ='Sorry, We cant find your City right now'

            else:
                err_msg = 'City already in List'
            
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added Successfully'
            message_class = 'is-success'
    
    
    form = CityForm()

    cities = City.objects.all()
    weather_data = []

    for city in cities:
        r = requests.get(url.format(city.name)).json()
        if r['cod'] == 200:  # Check if city is found

            city_weather = {
                'city': city.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
                'id': city.id,
            }
            weather_data.append(city_weather)
        else:
            print(f"Error retrieving weather data for {city.name}: {r}")

    weather_data.reverse()
    context = {
        'weather_data': weather_data,
          'form':form,
          'message':message,
          'message_class':message_class
        }
    return render(request, 'myapps/index.html', context)


def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('index')