# -*- coding: utf-8 -*-

class UrlBuilder(object):
    """
    Builds the API URL endpoints for the Cortex XDR's Python SDK.
    """
    fqdn = 'us'

    def __init__(self, fqdn):
        self.fqdn = fqdn

    def get_url(self, base, api_name, call_name):
        return base % (self.fqdn, api_name, call_name)

