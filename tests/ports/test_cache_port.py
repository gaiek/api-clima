from app.ports.cache_port import CachePort
from typing import Optional


def test_cache_port_executa_pass():
    class AdaptadorFalso(CachePort):
        def get(self, key: str) -> Optional[str]:
            super().get(key)
            return "valor_falso"
        
        def set(self, key: str, value: str, expire: int) -> None:
            super().set(key, value, expire)

    adaptador = AdaptadorFalso()
    adaptador.get("minha_chave")
    adaptador.set("minha_chave", "valor", 60)