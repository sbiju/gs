from django.conf.urls import url
from .views import VillaListApi, VillaCreateApi, VillaUpdateApi, VillaDetailApi, VillaDeleteApi


urlpatterns = [
    url(r'^api/$', VillaListApi.as_view(), name='api_list'),
    url(r'^api/(?P<pk>\d+)/$', VillaDetailApi.as_view(), name='api_detail'),
    url(r'^api/(?P<pk>\d+)/edit/$', VillaUpdateApi.as_view(), name='api_edit'),
    url(r'^api/(?P<pk>\d+)/delete/$', VillaDeleteApi.as_view(), name='api_delete'),
    url(r'^api/create/$', VillaCreateApi.as_view(), name='api_add'),
]