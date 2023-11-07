# Generated by Django 4.2.6 on 2023-11-06 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsdetail',
            name='goods_code',
        ),
        migrations.AddField(
            model_name='goodsdetail',
            name='goods',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='goodsdetail', to='goods.goods'),
        ),
    ]