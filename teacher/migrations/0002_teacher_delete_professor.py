# Generated by Django 4.1.3 on 2022-11-19 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price_per_hour', models.DecimalField(decimal_places=2, max_digits=9)),
                ('description', models.TextField()),
                ('picture', models.URLField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
    ]
