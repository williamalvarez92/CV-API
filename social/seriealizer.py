from rest_framework import serializers
from .models import Social

class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'