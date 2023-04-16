from rest_framework import serializers
from .models import *
from rest_framework.validators import ValidationError
from django.db.models import Avg


class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolim
        fields = '__all__'

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'

    def to_representation(self, instance):
        malumot = super().to_representation(instance)
        malumot['yangi_narx'] = instance.narx - (instance.narx/100 * instance.chegirma)
        izohlar = Izoh.objects.filter(mahsulot=instance)
        malumot['ortacha_reyting'] = round(izohlar.aggregate(Avg('reyting'))['reyting__avg'], 1)
        return malumot

class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = '__all__'

    def validate_reyting(self, reyting):
        if 1 <= reyting <= 5:
            return reyting
        raise serializers.ValidationError("Noto'g'ri reyting bal kiritildi")