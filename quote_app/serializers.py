from rest_framework import serializers
from .models import Writer, Quote

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = '__all__'

class QuoteSerializer(serializers.ModelSerializer):
    writer = WriterSerializer()

    class Meta:
        model = Quote
        fields = '__all__'
