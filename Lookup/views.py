from django.shortcuts import render
from django.views import View
import json
import requests


def index(request):
    zipcode = '20002'
    if request.method == 'POST':
        zipcode = request.POST['zipcode']
        
    description = 'Data is not available.'
    aqiColorState = 'Unavailable'

    try:
        result = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='+ zipcode +'&distance=25&API_KEY=4BA23550-77EA-4FC4-B3CD-C5609F54257D')
        api = json.loads(result.content)
        if api[0]['Category']['Number'] == 1:
            description = 'Air quality is satisfactory, and air pollution poses little or no risk.'
            aqiColorState = 'Good'
        
        elif api[0]['Category']['Number'] == 2:
            description = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution. '
            aqiColorState = 'Moderate'

        elif api[0]['Category']['Number'] == 3: 
            description = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
            aqiColorState = 'USG'

        elif api[0]['Category']['Number'] == 4:
            description = 'Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
            aqiColorState = 'Unhealthy'

        elif api[0]['Category']['Number'] == 5:
            description = 'Health alert: The risk of health effects is increased for everyone.'
            aqiColorState = 'VeryUnhealthy'
            
        elif api[0]['Category']['Number'] == 6: 
            description = 'Health warning of emergency conditions: everyone is more likely to be affected.'
            aqiColorState = 'Hazardous'

    except Exception as e:
        api = 'Error'

    return render(request, 'index.html', {
            'api': api,
            'aqiColorState': aqiColorState,
            'description': description
        })
        
    
class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
