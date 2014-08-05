from __future__ import (absolute_import, division,
                        print_function, unicode_literals)


import caniusepython3 as ciu

from . import utils



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


class pypi_scanner(object):
    def __init__(self):
        pass

    def _get_all_github_packages(self):
        with ciu.pypi.pypi_client() as client:
            list_of_packages = client.search({'home_page': 'github'})

        set_of_packages_names = [v['name'] for v in list_of_packages]
        return set_of_packages_names, list_of_packages

    def _get_all_python_packages(self):
        utils.get_pypi_package_data()

    def _get_all_python3_packages(self):
        pass

    def get_python2_only_packages(self):
        """
        returns a list of all PyPI packages that
        is python 2 compatible only.
        """
        python_packages = self._get_all_python_packages()
        python3_packages = self._get_all_python3_packages()
        python2_only_packages = python_packages.difference(python3_packages)
        return list(python2_only_packages)

    def get_python2_github_packages(self):
        python2_only_packages = set(self.get_python2_only_packages())
        github_packages, _ = self._get_all_github_packages()
        github_packages = set(github_packages)
        python2_github_packages = python2_only_packages.intersection(github_packages)
        return list(python2_github_packages)