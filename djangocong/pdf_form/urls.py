from django.conf.urls.defaults import patterns, url
from djangocong.pdf_form.views import ticket_print


urlpatterns = patterns('',
    url(r'^print/$', ticket_print, name='ticket-print'),
)
