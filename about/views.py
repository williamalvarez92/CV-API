from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import status

from .models import About
from .seriealizer import AboutSerializer

class AboutListView(APIView):

        def get(self, _request):
            abouts = About.object.all()
            serialized_about = AboutSerializer(abouts, many=True)
            return Response(serialized_about.data, status=status.HTTP_200_OK)