from django.db import reset_queries
from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView

from skill.seriealizer import SkillsSerializer
from .models import Skill
from rest_framework import status
from rest_framework.response import Response

class SkillsListView(APIView):

      def get(self, _request):
        skills = Skill.objects.all()
        skill_seriealizer = SkillsSerializer(skills, many=True)
        return Response(skill_seriealizer.data, status=status.HTTP_200_OK)