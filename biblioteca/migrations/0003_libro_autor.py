# Generated by Django 4.2.3 on 2023-10-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_alter_libro_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='autor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]