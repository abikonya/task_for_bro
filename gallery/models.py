from django.db import models
from time import strftime

# Saved image model


class Images(models.Model):
    name = models.CharField(max_length=50, default=strftime('%H:%M:%S'), verbose_name='Name')
    tags = models.CharField(max_length=50, null=True, verbose_name='Tag')
    image = models.ImageField(upload_to='{}'.format(strftime('%d%b%Y')), verbose_name='Image')
    created = models.DateTimeField(max_length=50, auto_now_add=True, db_index=True, verbose_name='Created')

    class Meta:
        verbose_name_plural = 'Images'
        verbose_name = 'Image'
        ordering = ['-created', '-name']