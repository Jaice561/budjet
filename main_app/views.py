from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Budget
# Create your views here.

def home(request):
    return render (request, 'home.html')

def budgets_index(request):
    budgets = Budget.objects.all()
    return render(request, 'budgets/index.html', {'budgets': budgets})

def budgets_detail(request, budget_id):
    budget = Budget.objects.get(id=budget_id)
    return render(request, 'budgets/detail.html', {'budget': budget})

class BudgetCreate(CreateView):
    model = Budget
    fields = '__all__'
    success_url = '/budgets/'

class BudgetDelete(DeleteView):
    model = Budget
    success_url = '/budgets/'