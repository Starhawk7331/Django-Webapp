# Generated by Django 4.2.5 on 2023-10-16 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_website", "0007_cat_pics_likes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cat_pics",
            name="likes",
        ),
        migrations.RemoveField(
            model_name="cat_pics",
            name="path",
        ),
        migrations.AddField(
            model_name="cat_pics",
            name="image",
            field=models.ImageField(default="", upload_to="test_website/images/cats/"),
        ),
        migrations.AddField(
            model_name="cat_pics",
            name="title",
            field=models.CharField(default="", max_length=30),
        ),
    ]