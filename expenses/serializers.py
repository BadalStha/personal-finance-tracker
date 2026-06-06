from rest_framework import serializers
from .models import Expense

class ExpenseSerializers(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Expense
        fields = ['id', 'title', 'amount', 'category', 'category_display', 'date']