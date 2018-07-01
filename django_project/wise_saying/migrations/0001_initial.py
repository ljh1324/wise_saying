# Generated by Django 2.0.6 on 2018-07-01 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=20)),
                ('member_password', models.CharField(max_length=40)),
                ('member_name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Saying',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.CharField(max_length=200)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wise_saying.Member')),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wise_saying.Member'),
        ),
        migrations.AddField(
            model_name='like',
            name='saying',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wise_saying.Saying'),
        ),
    ]
