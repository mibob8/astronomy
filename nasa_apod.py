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
    image_description = json.loads(response.text)['explanation']

    response = requests.get(image_path)
    image_bytes = io.BytesIO(response.content)

    image = Image.open(image_bytes)
    image.show()

    print_photo_information(str(date), image_description)


def print_photo_information(current_date: str, image_description: str):
    print('Current date: ' + current_date + '\n\n')
    print('Image description: ' + '\n')
    print(image_description + '\n\n')
    input('Press Enter to continue...')


get_apod()
