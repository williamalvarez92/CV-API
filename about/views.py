from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import About
from .seriealizer import AboutSerializer

class AboutListView(APIView):
      try:
        def get(self, _request):
            abouts = About.objects.all()
            print('jobroles', abouts)
            serialized_about = AboutSerializer(abouts, many=True)
            return Response(serialized_about.data, status=status.HTTP_200_OK)
      except About.DoesNotExist:
        raise NotFound(detail='Cannot find product')