# Generated by Django 4.0.3 on 2022-04-05 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_remove_profile_password_remove_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(upload_to='Images'),
        ),
    ]
