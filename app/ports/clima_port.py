from abc import ABC, abstractmethod
from app.domain.models import ClimaTempo

class ClimaPort(ABC):
    @abstractmethod
    def get_clima(self, location: str) -> ClimaTempo:
        pass