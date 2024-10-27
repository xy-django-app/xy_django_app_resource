# -*- coding: UTF-8 -*-

from django.contrib import admin
from .models import *

# Register your models here.
from django.utils.safestring import mark_safe


@admin.register(MPDFCollection)
class APDFCollection(admin.ModelAdmin):
    filter_horizontal = [
        "pdfs",
    ]


@admin.register(MPDF)
class APDF(admin.ModelAdmin):
    pass


@admin.register(MImageCollection)
class AImageCollection(admin.ModelAdmin):
    filter_horizontal = [
        "images",
    ]

@admin.register(MImage)
class AImage(admin.ModelAdmin):
    list_display = (
        "identifier",
        "id",
        "name",
    )
    readonly_fields = ("icon_preview",)
    search_fields = ["id", "name", "identifier"]

@admin.register(MAPackageCollection)
class APackageCollection(admin.ModelAdmin):
    filter_horizontal = [
        "packages",
    ]


@admin.register(MAPackage)
class APackage(admin.ModelAdmin):
    pass


@admin.register(MARequest)
class ARequest(admin.ModelAdmin):
    pass




class Response(admin.ModelAdmin):
    pass


admin.site.register(Response, ResponseAdmin)


class HTMLFile(admin.ModelAdmin):
    pass


admin.site.register(HTMLFile, HTMLFileAdmin)


class VideoCollection(admin.ModelAdmin):
    filter_horizontal = [
        "videos",
    ]


admin.site.register(VideoCollection, VideoCollectionAdmin)


class Video(admin.ModelAdmin):
    pass


admin.site.register(Video, VideoAdmin)


class AudioCollection(admin.ModelAdmin):
    filter_horizontal = [
        "audios",
    ]


admin.site.register(AudioCollection, AudioCollectionAdmin)


class Audio(admin.ModelAdmin):
    pass


admin.site.register(Audio, AudioAdmin)


class TextCollection(admin.ModelAdmin):
    filter_horizontal = [
        "texts",
    ]


admin.site.register(TextCollection, TextCollectionAdmin)


class Text(admin.ModelAdmin):
    pass


admin.site.register(Text, TextAdmin)
