# Generated by Django 3.1.5 on 2021-01-30 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210130_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.device'),
        ),
    ]