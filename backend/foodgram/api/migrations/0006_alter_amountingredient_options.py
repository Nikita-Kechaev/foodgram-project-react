# Generated by Django 4.0.4 on 2022-04-28 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_amountingredient_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amountingredient',
            options={'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиенты'},
        ),
    ]
