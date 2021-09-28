from django.db import models

# Create your models here.

class contact(models.Model):
    contact_name=models.CharField(max_length=100)
    contact_email=models.EmailField(max_length=100)
    contact_number=models.CharField(max_length=45)
    contact_message=models.TextField(max_length=254)

    def __str__(self):
        return f"Message from {self.contact_name}"