# Generated by Django 4.2 on 2023-04-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_link_alter_about_options_remove_about_icon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='icon',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Icon'),
        ),
    ]
