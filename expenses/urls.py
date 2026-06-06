from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/expenses/', views.expense_api, name='expense_api'),
    path('api/expenses/<int:pk>/', views.expense_detail_api, name='expense_detail_api'),
]