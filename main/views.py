from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class BolimAPI(APIView):
    def get(self, request):
        bolims = Bolim.objects.all()
        serializer = BolimSerializer(bolims, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BolimItems(APIView):
    def get(self, request, pk):
        try:
            bolim = Bolim.objects.get(id=pk)
            mahsulotlar = Mahsulot.objects.filter(bolim=bolim)
            serializer = MahsulotSerializer(mahsulotlar, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Bolim.DoesNotExist:
            return Response({"error": "Bolim topilmadi."}, status=status.HTTP_404_NOT_FOUND)


class IzohlarAPI(APIView):
    def get(self, request, pk):
        izohlar = Izoh.objects.filter(mahsulot_id=pk)
        serializer = IzohSerializer(izohlar, many=True)
        return Response(serializer.data)