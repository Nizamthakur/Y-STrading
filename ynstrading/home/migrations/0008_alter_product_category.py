# Generated by Django 4.2 on 2024-07-05 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Tank Top', 'Tank Top'), ('Swimwear', 'Swimwear'), ('Sundress', 'Sundress'), ('Bright', 'Bright'), ('Heavy Coat', 'Heavy Coat'), ('Gloves', 'Gloves'), ('Hats', 'Hats'), ('Thermal', 'Thermal'), ('Long Sleeves', 'Long Sleeves'), ('Sweaters', 'Sweaters'), ('jeans', 'jeans')], default='Men', max_length=20),
        ),
    ]
