from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from data_brewer.views import DataSourceViewSet

router = routers.SimpleRouter()
router.register(r'datasources', DataSourceViewSet)
router.register(r'datastreams', DataSourceViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
