from django.contrib import admin
from .models import Release
from django.db import models
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from ckeditor.widgets import CKEditorWidget


class ReleaseAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}

class FlatPageAdmin(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

admin.site.register(Release, ReleaseAdmin)

# workaround to get the flatpages app to use CKeditor
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)