from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('zombify.views',
    (r'^$', 'index'),
    (r'^result$', 'result'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^(?P<zomblink>\w+)$', 'redirect')
)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
)

