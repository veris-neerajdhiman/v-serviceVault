#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- service_vault.views
~~~~~~~~~~~~~~~~~~~~~~~~~~

- This file contains service-vault views means all http request/routers points to this file.
"""

# future
from __future__ import unicode_literals

# 3rd party
from django.http import HttpResponse
from rest_framework_proxy.views import ProxyView

# rest-framework
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status, views

# Django
from django.conf import settings

# local

# own app
from service_vault import models, serializers


class ServiceVaultViewSet(viewsets.ModelViewSet):
    """Service Vault Viewset, every resource http request handles by this class

    **Query Parameters**:
        `is_public` -- true/false, get public or private services only.

    - Two signals will be fired after a service is added.
      - One for adding Service in Kong
      - second for Register the Service for User on AM server if obj.assign_to_user is True

    - No Service can be updated once added,

    """
    model = models.ServiceVault
    queryset = model.objects.all()
    # TODO : remove AllowAny permission with proper permission class
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.ServiceVaultSerializer

    def get_queryset(self, *args, **kwargs):
        """
        Optionally restricts the returned services to public or private.
        by filtering against a `is_public` query parameter in the URL.
        """
        queryset = super(ServiceVaultViewSet, self).get_queryset(*args, **kwargs)
        if 'is_public' in self.request.query_params:
            if self.request.query_params.get('is_public') == 'true':
                queryset = queryset.filter(is_public=True)
            elif self.request.query_params.get('is_public') == 'false':
                queryset = queryset.filter(is_public=False)
        if 'names' in self.request.query_params:
            names = self.request.query_params.get('names').split(',')
            queryset = queryset.filter(name__in=names)
        return queryset

    def get_service_apis_from_kong(self, request, pk=None):
        """

        :param request: Django request param
        :param pk: service vault primary key
        :return: Service APIS or operations in swagger
        """
        response = self.get_object().get_operations()
        return Response({'operations': response}, status=status.HTTP_200_OK)


class ProxyKongView(ProxyView):
    """Proxy To kong

    """
    # ToDo: This a jugaad for kong Proxy, need to fix this asap.

    proxy_host = getattr(settings, 'KONG_SERVER')
    source = '{path}'

    def get_source_path(self):
        if self.source:
            return self.source.format(**self.kwargs)
        return None

    def get_headers(self, request):
        headers = super(ProxyKongView, self).get_headers(request)
        headers['HOST'] = request.META['HTTP_HOST_VERIS']
        return headers

    def create_response(self, response):
        if self.return_raw or self.proxy_settings.RETURN_RAW:
            return HttpResponse(response.text, status=response.status_code,
                    content_type=response.headers.get('content-type'))

        status = response.status_code

        # if status >= 400:
        #     body = {
        #         'code': status,
        #         'error': response.reason,
        #     }
        # else:
        #     body = self.parse_proxy_response(response)
        return Response(self.parse_proxy_response(response), status)

