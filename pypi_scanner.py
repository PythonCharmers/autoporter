from __future__ import (absolute_import, division,
                        print_function, unicode_literals)


import caniusepython3 as ciu

from . import utils
from . import classifier_finder


class pypi_scanner(object):
    def __init__(self):
        pass

    def _get_all_github_packages(self):
        with ciu.pypi.pypi_client() as client:
            list_of_packages = client.search({'home_page': 'github'})

        list_of_package_names = [v['name'] for v in list_of_packages]
        return list_of_package_names

    def _browse_classifier(self, classifiers):
        """
        classifiers - list of classifiers
        """

        with ciu.pypi.pypi_client() as client:
            list_of_packages = client.browse(list(classifiers))

        list_of_package_names = [v[0] for v in list_of_packages]
        return list_of_package_names

    def _get_all_python_packages(self):
        with ciu.pypi.pypi_client() as client:
            list_of_package_names = client.list_packages()

        return list_of_package_names

    def _get_all_python3_packages(self):
        c = classifier_finder('Programming Language :: Python :: 3')
        python_classifiers = c.get_classifiers()

        return self._browse_classifier()

    def _get_python2_only_packages(self):
        """
        returns a list of all PyPI packages that
        is python 2 compatible only.
        """
        python_packages = set(self._get_all_python_packages())
        python3_packages = set(self._get_all_python3_packages())
        python2_only_packages = python_packages.difference(python3_packages)
        return list(python2_only_packages)

    def get_python2_github_packages(self):
        """
        returns a list of python 2 only packages with github repos
        """
        python2_only_packages = set(self._get_python2_only_packages())
        github_packages = set(self._get_all_github_packages())
        python2_github_packages = python2_only_packages.intersection(github_packages)
        return list(python2_github_packages)