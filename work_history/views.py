from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Work
from .seriealizer import WorkSerializer

class WorkListView(APIView):
  
        def get(self, _request):
            works = Work.objects.all()
            serialized_work = WorkSerializer(works, many=True)
            return Response(serialized_work.data, status=status.HTTP_200_OK)