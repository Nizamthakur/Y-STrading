from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Tank Top', 'Tank Top'),
        ('Swimwear', 'Swimwear'),
        ('Sundress', 'Sundress'),
        ('Bright', 'Bright'),
        ('Heavy Coat', 'Heavy Coat'),
        ('Gloves', 'Gloves'),
        ('Hats', 'Hats'),
        ('Thermal', 'Thermal'),
        ('Long Sleeves', 'Long Sleeves'),
        ('Sweaters', 'Sweaters'),
        ('Jeans', 'Jeans'),
        # Add other categories as necessary
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Men')

    def __str__(self):
        return self.name