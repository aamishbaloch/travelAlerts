import json
import urllib
import requests

from geopy.geocoders import Nominatim

from BVGConnect.exceptions import ErrorInvalidInput, BVGError
from BVGConnect.settings import bvg_rest_url, geocoder_app_name


class BVGConnect:
    """
    BVGConnect is used to get more customized results from BVG rest API.
    """

    def __init__(self):
        self.base_url = bvg_rest_url
        self.geolocator = Nominatim(user_agent=geocoder_app_name)

    def get_earliest_journey_by_address(self, from_address, to_address):
        if not from_address:
            raise ErrorInvalidInput('Origin address missing')
        if not to_address:
            raise ErrorInvalidInput('Destination address missing')

        from_location = self.geolocator.geocode(from_address)
        to_location = self.geolocator.geocode(to_address)

        params = {
            'from.address': from_address,
            'from.latitude': from_location.latitude,
            'from.longitude': from_location.longitude,
            'from.type': 'location',
            'to.address': to_address,
            'to.latitude': to_location.latitude,
            'to.longitude': to_location.longitude,
            'to.type': 'location',
        }

        response = requests.get(
            f'https://1.bvg.transport.rest/journeys?{urllib.parse.urlencode(params)}'
        )
        data = json.loads(response.content.decode("utf-8"))

        if not response.status_code == 200:
            if 'msg' in data:
                raise BVGError(data['msg'])
            raise BVGError()

        data = data[0]['legs'] if len(data) > 0 else None

        route_points = []
        for item in data:
            if item['origin']['type'] == 'location':
                route_points.append(item['origin']['address'])
            elif item['origin']['type'] == 'stop':
                route_points.append(item['origin']['name'])
        route_points.append(to_address)

        journey = {
            'departure': data[0]['departure'],
            'arrival': data[len(data)-1]['arrival'],
            'route_points': route_points,
        }

        return journey
