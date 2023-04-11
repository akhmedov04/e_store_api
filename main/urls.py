from django.urls import path
from .views import *

urlpatterns = [
    path('bolimlar/', BolimAPI.as_view()),
    path('bolim/<int:pk>/mahsulotlar/', BolimItems.as_view()),
    path('mahsulot/<int:pk>/izohlar/', IzohlarAPI.as_view()),

]