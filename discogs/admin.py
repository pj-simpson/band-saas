from django.contrib import admin
from .models import Release

class ReleaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Release, ReleaseAdmin)