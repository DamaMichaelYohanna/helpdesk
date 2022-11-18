from django.db import models


class Issue(models.Model):
    """model for issue entry"""
    ref = models.CharField(max_length=10)
    complainant = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    complain = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.ref}'
