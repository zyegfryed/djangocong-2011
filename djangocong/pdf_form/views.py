# -*- coding: utf-8 -*-
from datetime import datetime

from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.template.defaultfilters import date

from pdf import get_template


def ticket_print(request, template_name='pdf_form/pdf/djangocong_ticket.pdf', **kwargs):
    ticket_number = '1320352209-28995359'

    context = {
        'event_label': _('Event'),
        'event_value': u'Rencontres Django 2011',
        'location_label': _('Location'),
        'location_value': u'Ecole Centrale de Marseille',
        'date_label': _('Date+Time'),
        'date_value': date(datetime.now(), 'SHORT_DATE_FORMAT'),
        'type_label': _('Type'),
        'type_value': u'Djangonaute Regular Ticket',
        'name_label': _('Name'),
        'name_value': u"Sébastien Fievet",
        'payment_label': _('Payment status'),
        'payment_value': _('PayPal Completed'),
    }

    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = \
        'attachment; filename=ticket-%s.pdf' % ticket_number

    template = get_template(template_name)
    response.write(template.render(context))

    return response
