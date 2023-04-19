from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from userapp.models import *

class BuyurtmaView(APIView):
    """
    Get or Create new Buyurtma
    """
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
    """
    Get or Create new SavatItem
    """
    def get(self, request):
        hoz_profil = Profil.objects.get(user=request.user)
        savat = Savat.objects.get(profil = hoz_profil)
        items = SavatItem.objects.filter(savat=savat)
        serializer = SavatItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SavatItemSerializer(data=request.data)
        savat = Savat.objects.get(profil=Profil.objects.get(user=request.user))
        if serializer.is_valid():
            serializer.save(savat=savat)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SavatItemEdit(APIView):
    """
    Edit or Delete SavatItem
    """
    def put(self, request, pk):
        savat_item = SavatItem.objects.get(pk=pk)
        serializer = SavatItemSerializer(savat_item, data=request.data)
        hoz_profil = Profil.objects.get(user=request.user)
        if savat_item.savat.profil == hoz_profil and serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        savat_item = SavatItem.objects.get(pk=pk)
        hoz_profil = Profil.objects.get(user=request.user)
        if savat_item.savat.profil == hoz_profil:
            savat_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

