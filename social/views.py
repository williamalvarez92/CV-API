# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView

from .seriealizer import SocialsSerializer
from .models import Social
from rest_framework import status
from rest_framework.response import Response

class SocialsSerializer(APIView):

      def get(self, _request):
        socials = Social.objects.all()
        socials_seriealizer = SocialsSerializer(socials, many=True)
        return Response(socials_seriealizer.data, status=status.HTTP_200_OK)