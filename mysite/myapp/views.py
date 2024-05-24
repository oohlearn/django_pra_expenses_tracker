from django.shortcuts import render
from .models import Expense

# Create your views here.


def list_view(request):
    expenses = Expense.objects.all()
    return render(request, 'myapp/index.html', {'expenses': expenses})