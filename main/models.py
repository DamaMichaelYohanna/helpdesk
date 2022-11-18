from django.db import models


class Issue(models.Model):
    """model for issue entry"""
    ref = models.CharField(max_length=10)
    complainant = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    complain = models.CharField(max_length=500)
    status_choice = [('Pending', 'Pending'),
                     ("Processing", "Processing"),
                     ('Resolved', 'Resolved'),
                     ('Failed', 'Failed')]
    status = models.CharField(max_length=15, choices=status_choice, default="Pending")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ref}'
