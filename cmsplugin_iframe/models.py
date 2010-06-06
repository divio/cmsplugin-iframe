from django.db import models
from cms.models import CMSPlugin

class IFrame(CMSPlugin):
    title = models.CharField(max_length=255, null=True, blank=True)
    width = models.PositiveSmallIntegerField(blank=True, null=True)
    height = models.PositiveSmallIntegerField()
    url = models.URLField()
    
    def __unicode__(self):
        return self.title
