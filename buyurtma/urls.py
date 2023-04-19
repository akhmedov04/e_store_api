from django.urls import path
from .views import *


urlpatterns = [
    path('', BuyurtmaView.as_view()),
    path('savat/', SavatItemsView.as_view()),
    path('savat/<int:pk>/', SavatItemEdit.as_view()),
]