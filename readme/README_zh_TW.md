<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:56
 * @FilePath: /xy_django_app_resource/readme/README_zh_TW.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_app_resource

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## 說明

通用資源資料模型.

## 程式碼庫

- <a href="https://github.com/xy-django-app/xy_django_app_resource.git" target="_blank">Github位址</a>  
- <a href="https://gitee.com/xy-opensource/xy_django_app_resource.git" target="_blank">Gitee位址</a>  
- <a href="https://gitcode.com/xy-opensource/xy_django_app_resource.git" target="_blank">GitCode位址</a>  

## 安裝

```bash
# bash
pip install xy_django_app_resource
```

## 使用


##### 1. 直接引入

- ###### 1. 設定全域配置

在Django專案中的settings.py檔案中加入如下配置
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
]

```

- ###### 2. 運行專案

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start

# 启动工程后访问 http://127.0.0.1:8401/admin 验证资源管理系统
```

##### 2. 自訂

- ###### 1. 建立Resource模組

> 操作 [範例工程](../samples/xy_web_server_demo/)

```bash
# bash
xy_web_server -w django startapp Resource
# Resource 模块创建在 source/Runner/Admin/Resource 
```

- ###### 2. 設定全域配置

在Django專案中的settings.py檔案中加入如下配置
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
    "Demo",
    "Media",
    "Resource",
]

```

- ###### 3. 在[Resource](../samples/xy_web_server_demo/source/Runner/Admin/Resource)模組的[models.py](../samples/xy_web_server_demo/source/Runner/Admin/Resource/models.py)檔中加入如下程式碼

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

- ###### 4. 在[Resource](../samples/xy_web_server_demo/source/Runner/Admin/Resource)模組的[admin.py](../samples/xy_web_server_demo/source/Runner/Admin/Resource/admin.py)檔中加入如下程式碼

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

- ###### 5. 運行專案

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start

# 启动工程后访问 http://127.0.0.1:8401/admin 验证资源管理系统
```

##### 運轉 [範例工程](../samples/xy_web_server_demo)

> 範例工程具體使用方式請移步 <b style="color: blue">xy_web_server.git</b> 下列倉庫
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github位址</a>  
> - <a href="https://gitee.com/xy-opensource/xy_web_server.git" target="_blank">Gitee位址</a>  
> - <a href="https://gitcode.com/xy-opensource/xy_web_server.git" target="_blank">GitCode位址</a>  

## 許可證
xy_django_app_resource 根據 <木蘭寬鬆許可證, 第2版> 獲得許可。有關詳細信息，請參閱 [LICENSE](../LICENSE) 文件。

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢?  

![Pay-Total](./Pay-Total.png)

## 聯繫方式

```
微信: yuyangiit
郵箱: yuyangit.0515@qq.com
```