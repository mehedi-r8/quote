from rest_framework import serializers
from .models import OppositeWord

class OppositeWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OppositeWord
        fields = ['word', 'opposite']
