# Generated by Django 4.0 on 2022-01-16 07:19

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Principal_Amount', models.CharField(max_length=11)),
                ('Intrest_Rate', models.CharField(max_length=5)),
                ('Given_Intrest', models.CharField(max_length=8)),
                ('Given_Principle', models.CharField(max_length=11)),
                ('Pending_Intrest', models.CharField(max_length=8)),
                ('Balance_Principle_Amount', models.CharField(max_length=11)),
                ('Case_N0', models.CharField(max_length=50)),
                ('Case_Type', models.CharField(max_length=10)),
                ('Case_link', models.CharField(max_length=200)),
                ('Person_Photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Person_Photo')),
                ('Pic_promissory_note', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Pic_promissory_note')),
                ('Pic_Id_Proof', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Pic_Id_Proof')),
                ('pic_Cheque', cloudinary.models.CloudinaryField(max_length=255, verbose_name='pic_Cheque')),
            ],
        ),
    ]
