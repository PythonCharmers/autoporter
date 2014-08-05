from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import unittest
from unittest.mock import patch

from .. import pypi_scanner
from .. import utils


class Test_pypi_scanner(unittest.TestCase):
    def setUp(self):
        self.iut = pypi_scanner.pypi_scanner()

    def tearDown(self):
        pass

    def test_github_packages_gets_returned(self):
        list_of_package_names = self.iut._get_all_github_packages()
        self.assertTrue(type(list_of_package_names[0]) == type(''))
        
        # just check the first in the list
        package = list_of_package_names[0]
        package_data = utils.get_pypi_package_data(package)
        github_url = utils.get_package_github_url(package_data)
        self.assertTrue(github_url)

    def test_browse_classifier(self):
        list_of_package_names = self.iut._browse_classifier(['Programming Language :: Python :: 3'])
        self.assertTrue(type(list_of_package_names[0]) == type(''))

        # just check the first in the list
        package = list_of_package_names[0]
        package_data = utils.get_pypi_package_data(package)
        support_py3 = utils.is_package_support_py3(package_data)
        self.assertTrue(support_py3)

    # def __

    # def test_get_python2_only_packages(self):
    #     with patch.object(self.iut, '_get_all_python_packages') as mock_method1:
    #         mock_method1.side_effect = 

    def test_get_all_python3_packages(self):
        expected_return_value = ['pk1','pk2']

        with patch.object(self.iut, '_browse_classifier') as mock_browse_classifier:
            mock_browse_classifier.return_value = expected_return_value
            list_of_package_names = self.iut._get_all_python3_packages()

            mock_browse_classifier.assert_called_once()
            self.assertEqual(expected_return_value, list_of_package_names)

if __name__ == '__main__':
    unittest.main()
