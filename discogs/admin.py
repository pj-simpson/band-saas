from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.utils.translation import gettext_lazy as _

from .models import Release, HomePage, Project, Format

from solo.admin import SingletonModelAdmin


class ReleaseAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}


class ProjectAdmin(admin.ModelAdmin):
    pass


class FormatAdmin(admin.ModelAdmin):
    pass


class FlatPageAdmin(FlatPageAdmin):
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}


admin.site.register(Release, ReleaseAdmin)
admin.site.register(Format, FormatAdmin)
admin.site.register(Project, ProjectAdmin)

# workaround to get the flatpages app to use CKeditor
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
