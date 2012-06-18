from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template',
        {'template': 'index.html'}, name='home'),
    (r'^', include('djangocong.pdf_form.urls')),
)

urlpatterns += staticfiles_urlpatterns()
