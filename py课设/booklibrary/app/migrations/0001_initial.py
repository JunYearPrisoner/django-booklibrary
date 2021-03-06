# Generated by Django 3.2.5 on 2022-06-07 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookName', models.CharField(max_length=64)),
                ('Author', models.CharField(max_length=64)),
                ('Price', models.CharField(max_length=64)),
                ('Publisher', models.CharField(max_length=255)),
                ('ISBN', models.CharField(max_length=255)),
                ('IsReadOnline', models.CharField(max_length=64)),
                ('BookNum', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Cord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.IntegerField(max_length=11)),
                ('BookName', models.IntegerField(max_length=11)),
                ('ReturnTime', models.DateTimeField()),
                ('State', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=64)),
                ('Email', models.CharField(max_length=64)),
                ('PassWord', models.CharField(max_length=64)),
                ('IsManager', models.IntegerField(max_length=11)),
            ],
        ),
    ]
