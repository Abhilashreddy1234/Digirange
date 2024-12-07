from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import Carousel, CarouselImage
@plugin_pool.register_plugin
class CarouselPlugin(CMSPluginBase):
    model = Carousel
    name = _("Carousel")
    render_template = "caurosal_plugin.html"
    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context
