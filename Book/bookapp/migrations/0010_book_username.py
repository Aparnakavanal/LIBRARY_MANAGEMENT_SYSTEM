# Generated by Django 4.0.3 on 2022-04-05 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0009_alter_book_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]