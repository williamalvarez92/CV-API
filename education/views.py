from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Education
from .seriealizer import EducationSerializer

class EducationListView(APIView):

        def get(self, _request):
            educations = Education.object.all()
            serialized_educations = EducationSerializer(educations, many=True)
            return Response(serialized_educations.data, status=status.HTTP_200_OK)