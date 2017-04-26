#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- service-vault.signals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- This file contains the Service-Vault app signals
"""

# future
from __future__ import unicode_literals

# 3rd party
import requests

# Django
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# local
from libs import kong

# own app
from service_vault.models import ServiceVault


@receiver(post_save, sender=ServiceVault)
def add_service_ob_to_kong(sender, instance, created=False, **kwargs):
    """Add service to kong

    :param sender: Signal sender
    :param instance: Service vault instance
    :param created: If new onj is created or updated
    :param kwargs: Signal kwargs
    """
    if created:
        kong.add_api(
            instance.name,
            instance.request_host,
            instance.upstream_url
        )


# @receiver(post_save, sender=ServiceVault)
# def add_service_ob_to_kong(sender, instance, created=False, **kwargs):
#     """Register service for Organization on AM server
#
#     :param sender: Signal sender
#     :param instance: Service vault instance
#     :param created: If new onj is created or updated
#     :param kwargs: Signal kwargs
#     """
#     if created and instance.assign_to_organization is True:
#         service_register_path = getattr(settings, 'AM_SERVER_SERVICE_REGISTER_PATH')
#
#         # replace SERVICE_UUID with service uuid
#         service_register_path = str(service_register_path).format(SERVICE_UUID=instance.uuid)
#
#         url = '{0}{1}'.format(getattr(settings, 'AM_SERVER_URL'),
#                               service_register_path)
#
#         data = {
#             "name": instance.name
#         }
#         data.update(**getattr(settings, 'DEFAULT_ORGANIZATION_SERVICE_PERM'))
#
#         # ToDo : Log Registering of service response somewhere
#
#         requests.post(url, json=data, verify=True)
#
