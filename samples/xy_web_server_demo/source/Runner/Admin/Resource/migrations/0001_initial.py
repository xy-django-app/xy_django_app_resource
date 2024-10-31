# Generated by Django 5.1.2 on 2024-10-31 12:09

import uuid
import xy_django_app_resource.abstracts
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MImage",
            fields=[
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=xy_django_app_resource.abstracts.images,
                        verbose_name="图片",
                    ),
                ),
                (
                    "url",
                    models.URLField(blank=True, null=True, verbose_name="图片链接"),
                ),
                (
                    "download_url",
                    models.URLField(blank=True, null=True, verbose_name="图片下载链接"),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="名称"
                    ),
                ),
                (
                    "width",
                    models.FloatField(blank=True, null=True, verbose_name="宽度"),
                ),
                (
                    "height",
                    models.FloatField(blank=True, null=True, verbose_name="高度"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="简介"),
                ),
                (
                    "path",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="路径"
                    ),
                ),
                (
                    "cdn_domain",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="CDN域名"
                    ),
                ),
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
            ],
            options={
                "verbose_name": "图片",
                "verbose_name_plural": "图片",
            },
        ),
    ]