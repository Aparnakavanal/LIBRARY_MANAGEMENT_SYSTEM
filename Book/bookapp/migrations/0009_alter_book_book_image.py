# Generated by Django 4.0.3 on 2022-04-05 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0008_alter_book_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.FileField(upload_to='images/'),
        ),
    ]
