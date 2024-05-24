# Generated by Django 5.0.6 on 2024-05-24 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('cost', models.IntegerField()),
                ('category', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]