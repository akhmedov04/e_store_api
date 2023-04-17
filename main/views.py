from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from userapp.models import *

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

    def post(self, request, pk):
        serializer = IzohSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(mahsulot=Mahsulot.objects.get(id=pk), profil=Profil.objects.get(user=request.user))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MahsulotAPI(APIView):
    def get(self, request, pk):
        mahsulot = Mahsulot.objects.get(id=pk)
        serializer = MahsulotSerializer(mahsulot)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MahsulotSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('qidirish')
        if query:
            mahsulot = Mahsulot.objects.filter(nom__icontains=query)
        else:
            mahsulot = Mahsulot.objects.all()
        serializer = MahsulotSearchSerializer(mahsulot, many=True)
        return Response(serializer.data)



class IzohDeleteAPI(APIView):
    def delete(self, request, pk):
        Izoh.objects.get(id=pk).delete()
        return Response({"success":"True"}, status=status.HTTP_200_OK)
