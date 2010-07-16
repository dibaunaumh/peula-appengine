from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from letters.models import Letter
from django.views.generic.list_detail import object_list
admin.autodiscover()

letters_list_info = {
    "queryset" : Letter.objects.all(),
    "template_name" : "list.html",
    "paginate_by" : 4,
}


urlpatterns = patterns('',
    # Example:
    # (r'^peula/', include('peula.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'organization/(?P<org>\w+)', 'letters.views.org_page'),

    (r'^api/search_similar_letters/(?P<prefix>\w+)', 'letters.views.search_similar_letters'),

    (r'^setup', 'letters.views.setup'),

    (r'^letter/add', 'letters.views.add_letter'),

    (r'^$', object_list, letters_list_info),
)
