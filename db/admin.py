import models
from django.contrib import admin

class ProjectImageInline(admin.StackedInline):
    model = models.ProjectImage
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('name', 'type', 'year', 'capacity',)
    list_filter = ('type', 'tags', 'authors',)
    search_fields = ['name']
    filter_horizontal = ('tags', 'authors', )

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']

class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Reference)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Project, ProjectAdmin)
