from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from app.models import Image
from app.utils import base64_to_image, image_to_base64
from django.contrib.auth import settings
import os


class SaveImageViewSet(ViewSet):

    def create(self, request):
        image = base64_to_image(request.data['file'])
        image_obj = Image.objects.create(

            image=image
        )
        image_url = str(settings.BASE_DIR) + image_obj.image.url
        if os.path.exists(image_url):
            base64_image_str = image_to_base64(image_url)
            image_url = 'http://' + request.get_host() + image_obj.image.url
            context = {
                'base64_image_str': base64_image_str,
                'image_url': image_url
            }
            return Response(context, status=status.HTTP_200_OK)

        return Response({'error': status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)

