# Generated by Django 4.2.1 on 2023-05-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_genre_alter_book_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
