# Generated by Django 2.0.6 on 2018-07-01 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wise_saying', '0004_auto_20180701_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saying',
            name='writer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wise_saying.Member'),
        ),
    ]