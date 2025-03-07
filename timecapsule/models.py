from django.db import models

class FutureMessage(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    delivery_date = models.DateTimeField()
    is_opened = models.BooleanField(default=False)
    