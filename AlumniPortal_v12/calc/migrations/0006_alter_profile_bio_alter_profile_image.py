# Generated by Django 5.1 on 2024-09-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0005_rename_dob_profile_date_of_birth_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
