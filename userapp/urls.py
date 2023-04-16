from django.urls import path
from .views import *

urlpatterns = [
    path('', UserCreateAPI.as_view()),
    path('profile/create/', ProfilCreateAPI.as_view()),
    path('logout/', LogoutView.as_view()),
    path('login/', LoginAPI.as_view()),
    path('profile/<int:pk>/', BittaProfilAPI.as_view()),
]