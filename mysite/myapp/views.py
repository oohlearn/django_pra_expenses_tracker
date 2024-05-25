from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
import datetime

# Create your views here.


def list_view(request):
    expenses = Expense.objects.all()
    form = ExpenseForm()
    total_expenses = expenses.aggregate(Sum('cost'))

    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year)
    year_sum = data.aggregate(Sum('cost'))

    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    month_sum = data.aggregate(Sum('cost'))

    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    week_sum = data.aggregate(Sum('cost'))

    daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(sum = Sum('cost'))
    # annotate(sum=Sum('cost')):
    # 使用 annotate 方法來對查詢集進行聚合操作。
    # Sum('cost') 計算每組 date 對應的 cost 字段的總和，並將結果儲存在 sum 字段中。
    
    category_sums = Expense.objects.filter().values('category').annotate(sum = Sum('cost'))

    if request.method == "POST":
        expense = ExpenseForm(request.POST)
        expense.save()
        return redirect("/")

    return render(request, 'myapp/index.html',
                  {'expenses': expenses,
                   "form": form,
                   "total_expenses": total_expenses,
                   "month_sum": month_sum,
                   "week_sum": week_sum,
                   "year_sum": year_sum,
                   "daily_sums": daily_sums,
                   "category_sums": category_sums})


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
