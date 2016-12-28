from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class API(models.Model):
    slug = models.CharField(max_length=123,help_text='api endpoint !')
    content = models.TextField(help_text='api json data format!')
    name = models.CharField(max_length=123,help_text='API Name!')

    class Meta:
        verbose_name = 'Mock_API'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('post_view', args=[self.slug])



