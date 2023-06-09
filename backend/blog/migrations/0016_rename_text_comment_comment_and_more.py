# Generated by Django 4.1.7 on 2023-03-30 02:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0015_rename_author_comment_commented"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="text",
            new_name="comment",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="parent_comment",
        ),
        migrations.AlterField(
            model_name="post",
            name="image_url",
            field=models.URLField(),
        ),
    ]
