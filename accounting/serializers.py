from rest_framework import serializers
from .models import Account, Customer, Supplier, Product, Transaction, TransactionLine


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        read_only_fields = ['user']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['user']


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ['user']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['user']


class TransactionLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionLine
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    lines = TransactionLineSerializer(many=True)

    class Meta:
        model = Transaction
        fields = ['id', 'user', 'date', 'description', 'reference', 'created_at', 'lines']
        read_only_fields = ['user', 'created_at', 'id']

    def create(self, validated_data):
        lines_data = validated_data.pop('lines')
        user = self.context['request'].user
        transaction = Transaction.objects.create(user=user, **validated_data)

        for line_data in lines_data:
            TransactionLine.objects.create(transaction=transaction, **line_data)

        # اینجا می‌توانی چک کنی جمع بدهکار == جمع بستانکار باشد

        return transaction
