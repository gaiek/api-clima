from app.application.clima_service import ClimaService
from unittest.mock import Mock
from app.domain.models import ClimaTempo

def test_get_clima_quando_cache_vazio():
    mock_cache_adapter = Mock()
    mock_clima_adapter = Mock()

    mock_cache_adapter.get.return_value = None

    clima_mock = ClimaTempo(
        location="Serranópolis de Minas, MG, Brasil",
        temperature=82.7,
        humidity=52.27,
        description="Rain, Overcast"
    )

    mock_clima_adapter.get_clima.return_value = clima_mock

    service = ClimaService(clima_adapter=mock_clima_adapter, cache_adapter=mock_cache_adapter)

    resultado = service.get_clima("Serranópolis de Minas, MG, Brasil")
    
    assert resultado.location == "Serranópolis de Minas, MG, Brasil"
    assert resultado.temperature == 82.7
    assert resultado.humidity == 52.27
    assert resultado.description == "Rain, Overcast"

    mock_cache_adapter.get.assert_called_once_with("clima:Serranópolis de Minas, MG, Brasil")
    mock_clima_adapter.get_clima.assert_called_once_with("Serranópolis de Minas, MG, Brasil")

    mock_cache_adapter.set.assert_called_once_with(
        key="clima:Serranópolis de Minas, MG, Brasil",
        value=clima_mock.model_dump_json(),
        expire=60
    )

def test_get_clima_quando_cache_preenchido():
    mock_cache_adapter = Mock()
    mock_clima_adapter = Mock()

    json_redis = '{"location": "Serranópolis de Minas, MG, Brasil", "temperature": 82.7, "humidity": 52.27, "description": "Rain, Overcast"}'

    mock_cache_adapter.get.return_value = json_redis

    service = ClimaService(clima_adapter=mock_clima_adapter, cache_adapter=mock_cache_adapter)

    resultado = service.get_clima("Serranópolis de Minas, MG, Brasil")
    assert resultado.location == "Serranópolis de Minas, MG, Brasil"
    assert resultado.temperature == 82.7
    assert resultado.humidity == 52.27
    assert resultado.description == "Rain, Overcast"

    mock_cache_adapter.get.assert_called_once_with("clima:Serranópolis de Minas, MG, Brasil")
    mock_clima_adapter.get_clima.assert_not_called()

    mock_cache_adapter.set.assert_not_called()