from rest_framework import serializers
from .models import *
from rest_framework.validators import ValidationError


class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolim
        fields = '__all__'

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'

class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = '__all__'

    def validate_reyting(self, reyting):
        if 1 > reyting > 5:
            raise serializers.ValidationError("Noto'g'ri reyting bal kiritildi")
        return reyting
