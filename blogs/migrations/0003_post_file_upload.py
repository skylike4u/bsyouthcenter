# Generated by Django 4.2 on 2024-09-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0002_category_subscriber_tag_alter_post_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="file_upload",
            field=models.FileField(blank=True, upload_to="files/%Y/%m/%d"),
        ),
    ]
