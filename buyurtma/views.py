from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from userapp.models import *

class BuyurtmaView(APIView):
    def get(self, request):
        hoz_profil = Profil.objects.get(user=request.user)
        buyurtmalar = Buyurtma.objects.filter(profil = hoz_profil)
        serializer = BuyurtmaSerializer(buyurtmalar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BuyurtmaSerializer(data=request.data)
        hoz_profil = Profil.objects.get(user=request.user)
        if serializer.is_valid():
            serializer.save(profil=hoz_profil)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SavatItemsView(APIView):
    def get(self, request):
        hoz_profil = Profil.objects.get(user=request.user)
        savat = Savat.objects.filter(profil = hoz_profil)
        items = SavatItem.objects.filter(savat=savat)
        serializer = SavatItemSerializer(items, many=True)
        return Response(serializer.data)