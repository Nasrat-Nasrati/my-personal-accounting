from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta
import random


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    google_id = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # وقتی createsuperuser می‌سازی

    def __str__(self):
        return self.email


class OTPCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otp_codes')
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    @classmethod
    def generate_code(cls):
        # کد ۶ رقمی تصادفی
        return f"{random.randint(100000, 999999)}"

    @property
    def is_expired(self):
        return self.created_at + timedelta(minutes=10) < timezone.now()

    def __str__(self):
        return f"{self.user.email} - {self.code}"
