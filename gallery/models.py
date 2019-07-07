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


# Settings model


class Settings(models.Model):
    KIND_OF_DISPLAY = (
        ('R', 'In a row'),
        ('L', 'As list')
    )
    METHODS = (
        ('RND', 'Random'),
        ('Num/Alph', 'Numeric/Alphabet'),
        ('D', 'By date')
    )
    display = models.CharField(max_length=60, choices=KIND_OF_DISPLAY, verbose_name='Display')
    number_displayed = models.IntegerField(blank=True, default=5, verbose_name='Quantity in a row/list')
    method = models.CharField(max_length=60, choices=METHODS, default='D', verbose_name='Sorting method')
    interval_for_slideshow = models.IntegerField(blank=True, default=3, verbose_name='Interval for slideshow in seconds')
    created = models.DateTimeField(max_length=50, auto_now_add=True, db_index=True, verbose_name='Created')

    class Meta:
        verbose_name_plural = 'Settings'
        verbose_name = 'Settings'
        ordering = ['-created', ]
