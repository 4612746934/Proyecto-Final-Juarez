# Generated by Django 4.2.6 on 2023-11-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='imagen',
        ),
        migrations.AddField(
            model_name='persona',
            name='apellido',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]