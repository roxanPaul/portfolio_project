# Generated by Django 4.2.11 on 2024-05-13 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_rename_company_experience_company_experience_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='email_contact',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='phone_contact',
        ),
        migrations.AddField(
            model_name='contact',
            name='address_contact',
            field=models.TextField(default=1234),
            preserve_default=False,
        ),
    ]
