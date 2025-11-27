from rest_framework import viewsets, permissions

from .models import Account, Customer, Supplier, Product, Transaction
from .serializers import (
    AccountSerializer,
    CustomerSerializer,
    SupplierSerializer,
    ProductSerializer,
    TransactionSerializer,
)


class UserOwnedModelViewSet(viewsets.ModelViewSet):
    """
    پایه تمام ویوست‌هایی که داده‌ها مربوط به user لاگین‌شده است.

    - هر یوزر فقط رکوردهای خودش را می‌بیند (get_queryset)
    - هنگام ساخت (create)، user به صورت خودکار از request.user ست می‌شود
    """

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # queryset اصلی را از کلاس فرزند می‌گیرد (مثلاً Account.objects.all())
        base_qs = super().get_queryset()
        # فیلتر فقط روی user لاگین‌شده
        return base_qs.filter(user=self.request.user)

    def perform_create(self, serializer):
        # در ساختن رکورد جدید، همیشه user = request.user
        serializer.save(user=self.request.user)


# -----------------------------
# Account
# -----------------------------
class AccountViewSet(UserOwnedModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# -----------------------------
# Customer
# -----------------------------
class CustomerViewSet(UserOwnedModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# -----------------------------
# Supplier
# -----------------------------
class SupplierViewSet(UserOwnedModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


# -----------------------------
# Product
# -----------------------------
class ProductViewSet(UserOwnedModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# -----------------------------
# Transaction
# -----------------------------
class TransactionViewSet(UserOwnedModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    # اینجا لازم نیست user را خودت ست کنی،
    # چون:
    #   - perform_create در UserOwnedModelViewSet صدا زده می‌شود
    #   - و TransactionSerializer.create هم از context['request'].user استفاده می‌کند.
    #
    # اگر خواستی صریح‌تر باشی، می‌توانی همین را نگه داری یا متد perform_create را حذف نکنی.
