import models
from django.contrib import admin

class ProjectImageInline(admin.StackedInline):
    model = models.ProjectImage
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('name', 'year')
    list_filters = ('year')
    search_fields = ['name']

admin.site.register(models.Author)
admin.site.register(models.Reference)
admin.site.register(models.Tag)
admin.site.register(models.Project, ProjectAdmin)
