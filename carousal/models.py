from django.db import models
from cms.models.pluginmodel import CMSPlugin
class Carousel(CMSPlugin):
    name = models.CharField(max_length=100)
class CarouselImage(models.Model):
    carousel = models.ForeignKey(Carousel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='carousel_images/')
    caption = models.CharField(max_length=255, blank=True)