from rest_framework import serializers
from .models import Antonym

class AntonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antonym
        fields = ['id', 'word', 'antonym']
