# Generated by Django 3.2.3 on 2021-07-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210704_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='data_comentario',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
