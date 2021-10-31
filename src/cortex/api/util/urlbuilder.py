# -*- coding: utf-8 -*-

class UrlBuilder(object):
    """
    Builds the API URL endpoints for the OneLogin's Python SDK.
    """
    fqdn = 'us'

    def __init__(self, fqdn):
        self.fqdn = fqdn

    def get_url(self, base, api_name=None, call_name=None):
        if api_name is None:
            return base % (self.fqdn)
        elif call_name is None:
            return base % (self.fqdn, api_name)
        else:
            return base % (self.fqdn, api_name, call_name)

