from rest_framework import serializers
from .models import Wine

class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = ('id',
                    'Name', 
                    'Winery',
                    'Variety',
                    'Image',
                    'Region',
                    'Description',
                    'Year',
                    'Totalqualifications',
                    'Avgqualifications',
                    'Score')