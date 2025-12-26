from django.http import JsonResponse
from django.shortcuts import render
from .utils import get_forecast

def predict_view(request):
    preds = get_forecast()
    return JsonResponse({"forecast": preds})

def home(request):
    return render(request, 'predictor/index.html')
