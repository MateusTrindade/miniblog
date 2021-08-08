# Generated by Django 3.2.3 on 2021-07-05 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20210630_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postagem',
            options={'ordering': ['-data_postagem']},
        ),
        migrations.AlterField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]