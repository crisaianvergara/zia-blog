# Generated by Django 4.1.7 on 2023-03-30 03:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0020_remove_comment_parent_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="created_date",
            new_name="date_commented",
        ),
    ]
