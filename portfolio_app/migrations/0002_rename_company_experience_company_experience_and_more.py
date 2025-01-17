# Generated by Django 4.2.11 on 2024-05-13 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='company',
            new_name='company_experience',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='title',
            new_name='title_experience',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='description',
            new_name='description_portfolio',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='url_portfolio',
            field=models.URLField(blank=True, null=True),
        ),
    ]
