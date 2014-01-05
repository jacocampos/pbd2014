from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tuloarmas.views.index', name='home'),
#    url(r'^$', 'tutoriales.views.index', name='home'),
    #url(r'^proyecto/', include('proyecto.foo.urls')),
    url(r'^productos/$', 'tuloarmas.views.productos'),
    url(r'^tutoriales/$', 'tuloarmas.views.tutoriales'),
    url(r'^login/$', 'tuloarmas.views.login_view'),
    url(r'^logout/$', 'tuloarmas.views.logout_view'),
    url('^home/$','tuloarmas.views.index'),
    url('^menu/$','tuloarmas.views.menu'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
