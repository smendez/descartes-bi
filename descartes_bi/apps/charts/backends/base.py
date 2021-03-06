from ast import literal_eval
import logging

from django.utils.translation import ugettext_lazy as _

logger = logging.getLogger(__name__)


class ChartBackend(object):
    """
    Base class for the chart rendering backend.
    """
    label = _('Chart base class')

    def __init__(self, report):
        self.report = report
        try:
            self.options = literal_eval(report.renderer_options)
        except Exception as exception:
            logger.error('Exception while evaluating renderer_options; %s' % exception)
            self.options = {}

        for option in self.__class__.options:
            setattr(self, option['name'], self.options.get(option['name']))

    def render(self, request):
        """Each backend must override this method. Method must return an
        HttpResponse or subclass, which is passed directly to the calling
        view.
        """
        raise NotImplemented
