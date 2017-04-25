#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- service_vault.router
~~~~~~~~~~~~~~

- THis file contains service vault router
"""

# future
from __future__ import unicode_literals

# 3rd party


# Django
from django.conf.urls import url

# local

# own app
from service_vault import views

vault_list = views.ServiceVaultViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
vault_detail = views.ServiceVaultViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})
vault_apis = views.ServiceVaultViewSet.as_view({
    'get': 'get_service_apis_from_kong',
})

urlpatterns = [
            url(r'^service/$',
                vault_list,
                name='service-vault-list'),
            url(r'^service/(?P<pk>[0-9]+)/$',
                vault_detail,
                name='service-vault-detail'),
            url(r'^service/(?P<pk>[0-9]+)/apis/$',
                vault_apis,
                name='service-vault-apis'),
]

