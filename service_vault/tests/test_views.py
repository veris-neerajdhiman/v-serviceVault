#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- service_vault.tests.test_views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- This file includes Test cases for Views .

"""

# future
from __future__ import unicode_literals

# 3rd party
import json, random

# Django
from django.test import TestCase
from django.core.urlresolvers import reverse
from urllib.parse import urlencode

# local
from service_vault.models import ServiceVault


class ServicevaultTestCase(TestCase):
    """Handles Vault Views Test Cases

    """

    def setUp(self):
        """

        """
        # ToDo : Move Registering Services on Kong to Platform. ONly Then below code can be un-commented.
        self.vault = object()
        # self.vault = ServiceVault.objects.create(
        #     name='test-name-{0}'.format(random.randint(1, 1000)),
        #     description='test-desc',
        #     request_host='local.test.com',
        #     upstream_url='http://local.test.in',
        #     swagger_schema={}
        # )

    def test_service_create(self):
        """Test Add service in vault

        """
        url = reverse('vault-urls:service-vault-list')
        data = {
            'name': 'test-template-{0}'.format(random.randint(1, 1000)),
            'description': 'template-desc',
            'request_host': 'local.test.com',
            'upstream_url': 'http://local.test.in',
            'swagger_schema': {}
        }
        pass
        # response = self.client.post(url, data=data)
        #
        # self.assertEqual(response.status_code, 201)

    def test_service_list(self):
        """Test Services list from vault

        """
        url = reverse('vault-urls:service-vault-list')

        response = self.client.get(url)
        pass
        # self.assertEqual(response.status_code, 200)

    def test_service_detail(self):
        """Test single service detail list

        """
        pass
        # url = reverse('vault-urls:service-vault-detail', args=(self.vault.uuid, ))
        #
        # response = self.client.get(url)
        # self.assertEqual(response.status_code, 200)

    def test_service_update(self):
        """Test Service partial Update

        """
        pass
        # url = reverse('vault-urls:service-vault-detail', args=(self.vault.uuid, ))
        #
        # data = urlencode({
        #     'name': 'updated-test'
        # })

        # response = self.client.patch(url, content_type="application/x-www-form-urlencoded", data=data)
        # self.assertEqual(response.status_code, 200)

    def test_service_delete(self):
        """Test Service delete

        """
        pass

        # url = reverse('vault-urls:service-vault-detail', args=(self.vault.uuid, ))
        #
        # response = self.client.delete(url)
        # self.assertEqual(response.status_code, 200)

    def test_vault_apis(self):
        """Test Service Vault API's list

        """
        pass
        # url = reverse('vault-urls:service-vault-apis', args=(self.vault.uuid, ))
        #
        # response = self.client.delete(url)
        # self.assertEqual(response.status_code, 200)