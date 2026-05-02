from django.utils import timezone
from django.db import models

# Create your models here.
class ChaiVarity(models.Model):
    
    CHAI_TYPE_CHOICES = [
        ('ML', 'Masala Chai'),
        ('GR', 'Ginger Chai'),
        ('CD', 'Cardamom Chai'),
        ('TS', 'Tulsi Chai'),
        ('LM', 'Lemon Chai'),
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chais/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name