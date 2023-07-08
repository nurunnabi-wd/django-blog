# Generated by Django 4.2.3 on 2023-07-08 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0003_alter_blog_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="status",
            field=models.CharField(
                choices=[("Draft", "draft"), ("Published", "published")],
                default="Draft",
                max_length=20,
            ),
        ),
    ]
