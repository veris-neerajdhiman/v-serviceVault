#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- service_vault.parsers
~~~~~~~~~~~~~~~~~~~~~~~

- This file contains Custom Parsers to render Response to clients
"""

# future
from __future__ import unicode_literals

# 3rd party

# rest-framework
from rest_framework.parsers import BaseParser

# Django

# local

# own app


class HTMLParser(BaseParser):
    """HTML parser.

    """
    media_type = 'text/html'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        return stream.read()


class PlainTextParser(BaseParser):
    """
    Plain text parser.
    """
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        return stream.read()
