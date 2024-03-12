from csv import DictReader
from django.core.management import BaseCommand
from django.contrib.gis.geos import Point
import requests
import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Import the model 
from world.models import Settlement

class Command(BaseCommand):
    # Show this when the user types help
    help = "Updates the data in the Settlement model"

    def handle(self, *args, **options):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        headers = {
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://aguaentucolonia.sacmex.cdmx.gob.mx/'
        }

        # make a call to retrieve the data from the url below replacing the id from 0 up to 2243
        for id in range(1, 2244):
            print("Processing id: %d" % id)
            url = "https://aguaentucolonia.sacmex.cdmx.gob.mx/api/v1/settlements/getSettlementsByIdForWaterInYourSettlement/%d" % id
            response = requests.get(url, headers=headers, verify=False)
            data = response.json()

            supply_zone = "Desconocida"
            if 'supply_zone' in data and data['supply_zone']:
                supply_zone = data['supply_zone']

            hours_of_service = "No disponible"
            if 'hours_of_service' in data and data['hours_of_service']:
                hours_of_service = data['hours_of_service']

            Settlement(
                day_measured = datetime.date.today(),
                identifier = id,
                settlement = data['settlement'],
                municipality = data['municipality'],
                supply_zone = supply_zone,
                is_atypical_condition = data['is_atypical_condition'],
                hours_of_service= hours_of_service,
                location=Point(float(data['longitude']), float(data['latitude']))
            ).save()
        
    
        

