from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('budgets/', views.budgets_index, name='index'),
    path('budgets/<int:budget_id>/', views.budgets_detail, name='detail'),
    path('budgets/create/', views.BudgetCreate.as_view(), name='budgets_create'),
    path('budgets/<int:pk>/delete/', views.BudgetDelete.as_view(), name='budgets_delete'),
]