# Generated by Django 2.2 on 2019-04-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('speed', models.DecimalField(decimal_places=2, max_digits=6)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=10)),
            ],
        ),
    ]
