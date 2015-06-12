""" urls """
from django.conf.urls import include, patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', 'shorten.views.index'),
                       (r'^result$', 'shorten.views.result'),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^(?P<code>\w+)$', 'shorten.views.send_away'),
                       )

urlpatterns += staticfiles_urlpatterns()
