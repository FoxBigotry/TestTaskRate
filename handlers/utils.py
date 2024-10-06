import requests
from settings import settings
from logs.logger import get_logger


logger = get_logger()


def get_dollar_rate():
    try:
        response = requests.get(settings.RATE)
        data = response.json()
        usd_rate = data['Valute']['USD']['Value']
        return round(usd_rate, 2)
    except Exception as e:
        logger.error(f"Ошибка при получении курса доллара: {e}")
        return None
