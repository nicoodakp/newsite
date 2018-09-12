from django.db import models
from django.conf import settings
from django.db.models import permalink
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from taggit.managers import TaggableManager


class PublicManager(models.Manager):
    def published(self):
        return self.get_queryset().filter(publish__lte=timezone.now())

class Post(models.Model):
    title = models.CharField(max_length = 130)
    updated = models.DateTimeField()
    body = models.TextField()
    allow_comments = models.BooleanField('allow comments', default=True)
    objects = PublicManager()
    tags = TaggableManager(blank = True)



    class Meta:
        db_table = 'simple_articles'
        ordering = ('-updated',)

    def __str__(self):
        return self.title

    def get_tag_list(self):
        return re.split(" ", self.tags)

    @permalink
    def get_absolute_url(self):
        return ("posts-post-detail", [self.pk])
