from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self): # python 2.7
        return self.title

    def __str__(self): # python 3.0
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={ 'id': self.id })
        # return "/posts/%s/" %(self.id)

    class Meta:
        ordering = ["-timestamp", 'updated']
