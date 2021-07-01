from rest_framework import serializers

from .models import Horse

class HorseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horse
        fields = ('id', 'name', 'age', 'breed', 'food', 'disease')