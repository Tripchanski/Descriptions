# Generated by Django 4.1.1 on 2023-02-15 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team2app', '0002_rename_content_item_description_remove_item_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
    ]