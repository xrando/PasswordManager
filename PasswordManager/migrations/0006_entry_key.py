# Generated by Django 4.1.10 on 2023-08-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PasswordManager', '0005_remove_entry_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='key',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
