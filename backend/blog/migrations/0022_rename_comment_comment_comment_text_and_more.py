# Generated by Django 4.1.7 on 2023-03-30 04:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0021_rename_created_date_comment_date_commented"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="comment",
            new_name="comment_text",
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="author",
            new_name="comment_user",
        ),
    ]
