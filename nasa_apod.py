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

    json_content = json.loads(response.text)

    image_path = json_content['url']
    image_description = json_content['explanation']

    response = requests.get(image_path)
    image_bytes = io.BytesIO(response.content)

    image = Image.open(image_bytes)
    image.show()

    print_photo_information(str(date), image_description)


def print_photo_information(current_date: str, image_description: str):

    message: str = f'''Current date: {current_date}

    Image description: 

    {image_description}

    '''

    print(message)

    input('Press Enter to continue...')


get_apod()
