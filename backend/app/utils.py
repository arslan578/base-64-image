import base64, secrets, io
from PIL import Image
from django.core.files.base import ContentFile


def base64_to_image(data_url):
    _format, _dataurl = data_url.split(';base64,')
    _filename, _extension = secrets.token_hex(20), _format.split('/')[-1]
    file = ContentFile(base64.b64decode(_dataurl), name=f"{_filename}.{_extension}")
    return file


def image_to_base64(image_url):

    with open(image_url, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string
