# Generated by Django 5.1.2 on 2024-10-31 12:09

import Media.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MMovie",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "update_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="更新时间"),
                ),
                (
                    "identifier",
                    models.UUIDField(
                        default=uuid.uuid4,
                        null=True,
                        unique=True,
                        verbose_name="唯一标识",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        blank=True, default=False, null=True, verbose_name="是否启用"
                    ),
                ),
                (
                    "movie",
                    models.FileField(
                        blank=True,
                        default=None,
                        help_text="图片",
                        null=True,
                        upload_to=Media.models.movies,
                        verbose_name="电影文件",
                    ),
                ),
            ],
            options={
                "verbose_name": "电影",
                "verbose_name_plural": "电影",
            },
        ),
    ]
