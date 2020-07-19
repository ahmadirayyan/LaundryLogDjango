from django.db import models
from datetime import datetime

# Create your models here.
class Items(models.Model):
    category_choices = (
        ('tshirt', 'tshirt'),
        ('shirt', 'shirt'),
        ('jacket', 'jacket'),
        ('sweatshirt', 'sweatshirt'),
        ('underwear', 'underwear'),
        ('shorts', 'shorts'),
        ('jeans', 'jeans'),
        ('pants', 'pants'),
        ('socks', 'socks'),
        ('mask', 'mask'),
        ('towel', 'towel'),
        ('bedsheet', 'bedsheet'),
        ('etc', 'etc'),
    )
    color_choices = (
        ('white', 'white'),
        ('grey', 'grey'),
        ('black', 'black'),
        ('red', 'red'),
        ('orange', 'orange'),
        ('yellow', 'yellow'),
        ('green', 'green'),
        ('blue', 'blue'),
        ('purple', 'purple')
    )
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=20, choices=category_choices)
    color = models.CharField(max_length=20, choices=color_choices)
    brand = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    desc = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    datebought = models.DateTimeField(default=datetime.utcnow)
    created_at = models.DateTimeField(default=datetime.utcnow)
    updated_at = models.DateTimeField(default=datetime.utcnow)