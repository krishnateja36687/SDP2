# Generated by Django 3.2.3 on 2021-05-17 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100)),
                ('mobileno', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('cpassword', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('account', models.CharField(choices=[('Savings', 'Savings'), ('Current', 'Current'), ('Salary', 'Salary')], max_length=100)),
            ],
            options={
                'db_table': 'sdpproject',
            },
        ),
    ]
