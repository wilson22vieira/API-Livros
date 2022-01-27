# Generated by Django 4.0.1 on 2022-01-27 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_books_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
