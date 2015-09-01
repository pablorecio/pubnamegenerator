from django.views.generic import TemplateView

from .generator import generate_pub_name


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(IndexView, self).get_context_data(*args, **kwargs)
        ctx.update({
            'pub_name': generate_pub_name(),
        })
        return ctx
