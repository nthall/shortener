from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'zombify.views.index'),
    (r'^result$', 'zombify.views.result'),
    (r'^admin/', include(admin.site.urls)),
    (r'^(?P<zomblink>\w+)$', 'zombify.views.redirect'),
)
