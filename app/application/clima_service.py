from app.ports.clima_port import ClimaPort
from app.ports.cache_port import CachePort
from app.domain.models import ClimaTempo

class ClimaService:
    def __init__(self, clima_adapter: ClimaPort, cache_adapter: CachePort):
        self.clima_adapter = clima_adapter
        self.cache_adapter = cache_adapter

    def get_clima(self, location: str) -> ClimaTempo:
        cache_key = f"clima:{location}"
        cached_data = self.cache_adapter.get(cache_key)
        
        if cached_data:
            return ClimaTempo.model_validate_json(cached_data)
        
        clima_tempo = self.clima_adapter.get_clima(location)
        self.cache_adapter.set(
            key=cache_key,
            value=clima_tempo.json(),
            expire=60)
        
        return clima_tempo
