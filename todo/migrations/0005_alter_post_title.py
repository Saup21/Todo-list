# Generated by Django 3.2.1 on 2021-05-12 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
