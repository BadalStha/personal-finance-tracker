from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Expense
from .serializers import ExpenseSerializers

# Create your views here.
def dashboard(request):
    return render(request, 'expenses/dashboard.html')