from app.ports.clima_port import ClimaPort
from app.domain.models import ClimaTempo

def test_clima_port_executa_pass():
    class AdaptadorFalso(ClimaPort):
        def get_clima(self, location: str) -> ClimaTempo:
            super().get_clima(location) 
            return ClimaTempo(location="Teste", temperature=0, humidity=0, description="Teste")

    adaptador = AdaptadorFalso()
    adaptador.get_clima("Qualquer lugar")