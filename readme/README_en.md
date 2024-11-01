<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:22
 * @FilePath: /xy_django_app_resource/readme/README_en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_app_resource

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## Description

Backend account data model.

## Source Code Repositories

- <a href="https://github.com/xy-django-app/xy_django_app_resource.git" target="_blank">Github</a>  
- <a href="https://gitee.com/xy-django-app/xy_django_app_resource.git" target="_blank">Gitee</a>

## Installation

```bash
# bash
pip install xy_django_app_resource
```

## How to use

##### 1. 直接引入

- ###### 1. 设置全局配置

在Django项目中的settings.py文件中加入如下配置
例如: [settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

```python
# settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "xy_django_app_resource",
    "Demo",
    "Media",
    "Resource",

```

- ###### 2. 运行项目

```bash
xy_web_server -w django start
# 启动工程后访问 http://127.0.0.1:8401/admin 验证资源管理系统
```

##### 2. 自定义

- ###### 1. 创建Resource模块

> 操作 [样例工程](../samples/xy_web_server_demo/)

```bash
# bash
xy_web_server -w django startapp Resource
# Resource 模块创建在 source/Runner/Admin/Resource 
```

- ###### 2. 设置全局配置

在Django项目中的settings.py文件中加入如下配置
例如: [settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

```python
# settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "xy_django_app_resource",
    "Demo",
    "Media",
    "Resource",
]

```

- ###### 3. 在[Resource](../samples/xy_web_server_demo/source/Runner/Admin/Resource)模块的[models.py](../samples/xy_web_server_demo/source/Runner/Admin/Resource/models.py)文件中加入如下代码

```python
# models.py

import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models
from xy_django_app_resource.abstracts import MAImage


class MImage(MAImage):
    id = models.BigAutoField(primary_key=True)
    create_at = models.DateTimeField(
        verbose_name=_("创建时间"),
        auto_now_add=True,
        editable=True,
    )
    update_at = models.DateTimeField(
        verbose_name=_("更新时间"),
        auto_now_add=True,
        editable=True,
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        default=uuid.uuid4,
        editable=True,
        unique=True,
        null=True,
    )
    is_active = models.BooleanField(
        verbose_name=_("是否启用"),
        null=True,
        blank=True,
        default=False,
    )

    class Meta:
        verbose_name = _("图片")
        verbose_name_plural = _("图片")
        app_label = "Resource"

    def __str__(self):
        return f"{self.id}. {self.identifier}"


```

- ###### 4. 在[Resource](../samples/xy_web_server_demo/source/Runner/Admin/Resource)模块的[admin.py](../samples/xy_web_server_demo/source/Runner/Admin/Resource/admin.py)文件中加入如下代码

```python
# admin.py
from django.contrib import admin
from .models import MImage

@admin.register(MImage)
class AImage(admin.ModelAdmin):
    list_per_page = 20
    filter_horizontal = []
    list_display_links = [
        "id",
        "identifier",
        "update_at",
        "create_at",
    ]
    list_display = [
        "id",
        "identifier",
        "update_at",
        "create_at",
    ]
    search_fields = list_display
    autocomplete_fields = [
        # "id",
        # "communicate_at",
        # "identifier",
    ]

```

- ###### 5. 运行项目

```bash
xy_web_server -w django start
# 启动工程后访问 http://127.0.0.1:8401/admin 验证资源管理系统
```

##### Run [Sample Project](../samples/xy_web_server_demo)

> For detailed usage of the sample project, please go to the following repository <b style="color: blue">xy_web_server.git</b> 
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github</a>  
> - <a href="https://gitee.com/xy-web-service/xy_web_server.git" target="_blank">Gitee</a>

## License
xy_django_app_resource is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![Pay-Total](./Pay-Total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```