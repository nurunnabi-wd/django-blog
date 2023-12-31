# Generated by Django 4.2.3 on 2023-07-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0002_alter_category_options_blog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="status",
            field=models.IntegerField(
                choices=[("Draft", "draft"), ("Published", "published")],
                default="Draft",
                max_length=20,
            ),
        ),
    ]
