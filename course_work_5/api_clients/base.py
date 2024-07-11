from abc import ABC, abstractmethod
import requests
import json


class APIClient(ABC):
    """Базовый класс для класса HeadHunterAPIClient"""

    @property
    @abstractmethod
    def base_url(self) -> str:
        pass

    def _get(self, url: str, params: dict = {}) -> dict:
        full_url = self.base_url + url

        response = requests.get(full_url, params=params, timeout=3)
        response.raise_for_status()
        return response.json()

