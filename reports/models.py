from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class SavedReport(models.Model):
    REPORT_TYPES = (
        ('BALANCE_SHEET', 'Balance Sheet'),
        ('INCOME_STATEMENT', 'Income Statement'),
        ('CUSTOM', 'Custom'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_reports')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=REPORT_TYPES)
    filters = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
