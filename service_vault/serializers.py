#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- service_vault.serializers
~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
    uuid = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.ServiceVault
        exclude = ('id', 'user', )

    def create(self, validated_data):
        """

        :param validated_data: Validated data
        :return: vault obj
        """
        user = self.context.get('request').user

        validated_data.update({
            'user': user
        })

        return models.ServiceVault.objects.create(**validated_data)
