from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors')
    website = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    year = models.IntegerField()
    month = models.IntegerField()
    capacity = models.IntegerField()
    width = models.FloatField()
    height = models.FloatField()
    depth = models.FloatField()
    stocks = models.IntegerField()
    annotation = models.TextField()
    location = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    authors = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images')
    image = models.ImageField(upload_to='projects')

    def __unicode__(self):
        return self.image.file.name

class Reference(models.Model):
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    project = models.ForeignKey(Project, related_name='references')

    def __unicode__(self):
        return self.name
