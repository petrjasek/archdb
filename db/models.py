from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors', blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Project(models.Model):

    TYPE_CHOICES = (
        ('project', 'Project'),
        ('realization', 'Realization'),
    )

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, blank=True, null=True)
    client = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    stocks = models.IntegerField(blank=True, null=True)
    annotation = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    authors = models.ManyToManyField(Author, blank=True, null=True)

    def __unicode__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images')
    image = models.ImageField(upload_to='projects')

    def __unicode__(self):
        return self.image.file.name

class Reference(models.Model):
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    project = models.ForeignKey(Project, related_name='references')

    def __unicode__(self):
        return self.name
