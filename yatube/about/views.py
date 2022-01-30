from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    """ Page author view. """
    template_name = 'about/author.html'


class AboutTechView(TemplateView):
    """Page tech view. """
    template_name = 'about/tech.html'
