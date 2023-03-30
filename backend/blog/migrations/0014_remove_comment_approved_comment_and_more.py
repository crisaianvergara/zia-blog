# Generated by Django 4.1.7 on 2023-03-30 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0013_rename_commented_comment_author_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="approved_comment",
        ),
        migrations.AddField(
            model_name="comment",
            name="parent_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="blog.comment",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="image_url",
            field=models.CharField(max_length=250),
        ),
    ]