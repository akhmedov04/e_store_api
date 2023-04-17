from rest_framework import serializers
from .models import *

class SavatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savat
        fields = '__all__'

    # def to_representation(self, instance):
    #     malumot = super().to_representation(instance)
    #     narx = instance.mahsulot.narx - (instance.mahsulot.narx / 100 * instance.mahsulot.chegirma)
    #     malumot['umumiy_narx'] = narx * instance.miqdor
    #     return malumot

class SavatItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavatItem
        fields = '__all__'

class TanlanganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanlangan
        fields = '__all__'

class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'