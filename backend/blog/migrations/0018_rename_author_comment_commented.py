# Generated by Django 4.1.7 on 2023-03-30 03:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0017_rename_commented_comment_author"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="author",
            new_name="commented",
        ),
    ]
