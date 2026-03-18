import requests
from app.ports.clima_port import ClimaPort
from app.domain.models import ClimaTempo


class VisualCrossingAdapter(ClimaPort):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={api_key}"

    def get_clima(self, location: str) -> ClimaTempo:
        url = self.base_url.format(api_key=self.api_key, location=location)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        clima_tempo = ClimaTempo(
            location=data['resolvedAddress'],
            temperature=data['currentConditions']['temp'],
            humidity=data['currentConditions']['humidity'],
            description=data['currentConditions']['conditions']
        )
        
        return clima_tempo