from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Portfolio
from .seriealizer import PortfolioSerializer

class PortfolioListView(APIView):

        def get(self, _request):
            portfolios = Portfolio.objects.all()
            serialized_educations = PortfolioSerializer(portfolios, many=True)
            return Response(serialized_educations.data, status=status.HTTP_200_OK)