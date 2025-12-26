from django.urls import path
from .views import predict_view, home

urlpatterns = [
    path('', home, name='home'),          # website
    path('predict/', predict_view),       # API
]
