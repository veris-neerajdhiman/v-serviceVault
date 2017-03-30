#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- service_vault.serializers
~~~~~~~~~~~~~~

- This file contains Service Vault app serializers
"""

# future
from __future__ import unicode_literals

# 3rd party


# Django
from rest_framework import serializers

# local


# own app
from service_vault import models


class ServiceVaultSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = models.ServiceVault
        exclude = ('created_at', 'modified_at', )
