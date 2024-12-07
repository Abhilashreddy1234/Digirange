from django.contrib import admin
from .models import Carousel, CarouselImage
class CarouselImageInline(admin.StackedInline):
    model = CarouselImage
    extra = 1 
class CarouselAdmin(admin.ModelAdmin):
    inlines = [CarouselImageInline]
    list_display = ['name'] 
admin.site.register(Carousel,CarouselAdmin)
