from django.shortcuts import render
from .models import *
from buyurtma.models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout



class UserCreateAPI(APIView):
    """
    To create a new user
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfilCreateAPI(APIView):
    """
    To create a new profile
    """
    def post(self, request):
        serializer = ProfilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Savat.objects.create(profil=Profil.objects.last())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BittaProfilAPI(APIView):
    """
    To get one profile
    """
    def get(self, request, pk):
        profil = Profil.objects.get(id=pk)
        serializer = ProfilSerializer(profil)
        return Response(serializer.data)

class LoginAPI(APIView):
    """
    To log in the user to the system
    """
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username = serializer.data['username'],
                password = serializer.data['password']
            )
            if user is None:
                return Response({"xabar":"Bunday user yo'q"}, status=status.HTTP_400_BAD_REQUEST)
            login(request, user)
            return Response({"xabar":"Tizimga muvaffaqqiyatli kirildi!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors)

class LogoutView(APIView):
    """
    To remove the user from the system
    """
    def get(self, request):
        logout(request)
        return Response({"xabar":"Foydalanuvchi tizimdan chiqarildi!"}, status=status.HTTP_200_OK)

class ProfileDetailAPIView(APIView):
    """
    Get, update, or delete a single profile instance.
    """
    def get_object(self, user):
        try:
            return Profil.objects.get(user=user)
        except Profil.DoesNotExist:
            return None

    def get(self, request):
        profil = self.get_object(request.user)
        if profil:
            serializer = ProfilSerializer(profil)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        profil = self.get_object(request.user)
        if profil:
            serializer = ProfilSerializer(profil, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        profil = self.get_object(request.user)
        if profil:
            profil.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)