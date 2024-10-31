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

#### 1. Create the Resource module
> Operation [Sample Project](../samples/xy_web_server_demo/)

```bash
# bash
xy_web_server -w django startapp Resource
# Resource Module created in source/Runner/Admin/Resource 
```

#### 2. The [settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py) in the sample project are as follows

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

#### 3. Add the following code to the [models.py](../samples/xy_web_server_demo/source/Runner/Admin/Resource/models.py) file of the [Resource](../samples/xy_web_server_demo/source/Runner/Admin/Resource) module

```python
# models.py
from xy_django_app_resource.abstracts import MARegion
from django.utils.translation import gettext_lazy as _

class MRegion(MARegion):
    class Meta:
        app_label = "Resource"
        verbose_name = _("地理信息")
        verbose_name_plural = _("地理信息")

```

#### 4. Add the following code to the[admin.py](../samples/xy_web_server_demo/source/Runner/Admin/Resource/admin.py) file of the [Resource](../samples/xy_web_server_demo/source/Runner/Admin/Resource) module

```python
# admin.py
from django.contrib import admin
from .models import MRegion

@admin.register(MRegion)
class ARegion(admin.ModelAdmin):
    pass

```

#### 5. Run the project

```bash
xy_web_server -w django start
# After starting the project, visit http://127.0.0.1:8401/admin to verify the Resource management system
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