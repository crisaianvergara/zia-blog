# Generated by Django 4.1.7 on 2023-03-30 03:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0016_rename_text_comment_comment_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="commented",
            new_name="author",
        ),
    ]
