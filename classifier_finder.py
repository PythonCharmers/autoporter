from __future__ import unicode_literals

import concurrent.futures
import contextlib
import json
import logging
import multiprocessing
import pkgutil
import re
import pickle

try:
    import urllib.request as urllib_request
except ImportError:  #pragma: no cover
    import urllib2 as urllib_request
import xml.parsers.expat
try:
    import xmlrpc.client as xmlrpc_client
except ImportError:  #pragma: no cover
    import xmlrpclib as xmlrpc_client


"""
"""
class classifier_finder(object):
    """
    Usage: 

    to find Python 2 classifiers:
        c = classifier_finder("Programming Language :: Python")

    to find Python 3 classifiers: 
        c = classifier_finder("Programming Language :: Python :: 3")
    """
    def __init__(self,  base_classifier):
        self.base_classifier = base_classifier

    def _get_classifier(self):
        """Fetch specified classifiers."""
        url = 'https://pypi.python.org/pypi?%3Aaction=list_classifiers'
        response = urllib_request.urlopen(url)
        try:
            try:
                status = response.status
            except AttributeError:  #pragma: no cover
                status = response.code
            if status != 200:  #pragma: no cover
                msg = 'PyPI responded with status {0} for {1}'.format(status, url)
                raise ValueError(msg)
            data = response.read()
        finally:
            response.close()
        classifiers = data.decode('utf-8').splitlines()
        return (classifier for classifier in classifiers
                if classifier.startswith(self.base_classifier))
