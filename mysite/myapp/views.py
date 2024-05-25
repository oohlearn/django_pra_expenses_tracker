from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

# Create your views here.


def list_view(request):
    expenses = Expense.objects.all()
    form = ExpenseForm()
    if request.method == "POST":
        expense = ExpenseForm(request.POST)
        expense.save()
        return redirect("/")

    return render(request, 'myapp/index.html', {'expenses': expenses,
                                                "form": form})


def edit(request, id=id):
    expense = Expense.objects.get(id=id)
    form = ExpenseForm(instance=expense)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, 'myapp/edit.html', {'form': form})


def delete(request, id=id):
    if request.method == "POST" and "delete" in request.POST:
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect("/")
