from abc import ABC, abstractmethod
from typing import Optional

class CachePort(ABC):
    @abstractmethod
    def get(self, key: str) -> Optional[str]:
        pass

    @abstractmethod
    def set(self, key: str, value: str, expire: int) -> None:
        pass