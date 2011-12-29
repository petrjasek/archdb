import models
from django.contrib import admin

class ProjectImageInline(admin.TabularInline):
    model = models.ProjectImage
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    ordering = ('name',)
    inlines = [ProjectImageInline]
    list_display = ('name', 'type', 'get_authors', 'year', 'state', 'capacity')
    list_filter = ('type', 'tags__name', 'authors__name')
    search_fields = ['name']
    filter_horizontal = ('tags', 'authors', 'constructions')

    def get_authors(self, project):
        for author in project.authors.all():
            return '%s' % (author.name)
    get_authors.short_description = 'Author'

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']

class TagAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ['name']

class ConstructionAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ['name']

admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Reference)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Construction, ConstructionAdmin)
admin.site.register(models.Project, ProjectAdmin)
