# Generated by Django 4.1.3 on 2022-12-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_confirmpassword_forgot_password_otp_signin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30, null=True)),
                ('emailid', models.EmailField(max_length=255)),
                ('date_of_birth', models.DateField(max_length=10)),
                ('gender', models.CharField(max_length=25)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=25, null=True)),
                ('password', models.CharField(max_length=10)),
                ('confirm_password', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameModel(
            old_name='Otp',
            new_name='SignUpOtp',
        ),
        migrations.DeleteModel(
            name='Confirmpassword',
        ),
        migrations.DeleteModel(
            name='Forgot_password',
        ),
        migrations.DeleteModel(
            name='Signin',
        ),
    ]
