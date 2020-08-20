from json.decoder import JSONDecoder
import requests
import json
from PIL import Image
import io
from datetime import datetime

from requests.models import Response


def get_apod():
    URL_APOD = "https://api.nasa.gov/planetary/apod"

    date = datetime.date(datetime.now())
    params = {
        'api_key': 'DEMO_KEY',
        'date': date,
        'hd': 'True'
    }
    response: Response = requests.get(URL_APOD, params=params)

    image_path = json.loads(response.text)['url']

    response = requests.get(image_path)
    image_bytes = io.BytesIO(response.content)

    image = Image.open(image_bytes)
    image.show()


get_apod()
