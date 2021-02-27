from django.contrib import admin
from .models import Release

class ReleaseAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Release, ReleaseAdmin)