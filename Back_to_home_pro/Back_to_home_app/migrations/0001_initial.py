# Generated by Django 4.2.5 on 2023-09-16 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='imagesmodel/')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField()),
                ('phonenumber2', models.IntegerField()),
                ('code', models.IntegerField()),
            ],
        ),
    ]
