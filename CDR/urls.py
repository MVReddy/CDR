from django.views.generic.simple import redirect_to
from django.conf.urls import patterns, include, url
from cdr_graph import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CDR.views.home', name='home'),
    # url(r'^CDR/', include('CDR.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    #url(r'^line-graph/(?P<date>.+)/$', views.draw_line_graph),
    #url(r'^pie-chart/(?P<date>.+)/$', views.draw_line_graph),
    url(r'^line-graph/$', views.draw_line_graph),
    url(r'^pie-chart/$', views.draw_pie_chart),
)
