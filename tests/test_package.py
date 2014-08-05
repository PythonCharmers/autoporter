import unittest

from future.standard_library import hooks
with hooks():
    from unittest.mock import patch, MagicMock

from utils import get_pypi_package_data, is_package_support_py3, \
    get_package_github_url


class TestPackageData(unittest.TestCase):
    def test_is_package_support_py3(self):
        self.assertEqual(is_package_support_py3(
            {'classifiers': ['Programming Language :: Python']}),
            False)

        self.assertEqual(is_package_support_py3(
            {'classifiers': ['Programming Language :: Python :: 2.7']}),
            False)

        self.assertEqual(is_package_support_py3(
            {'classifiers': ['Programming Language :: Python :: 3']}),
            True)

        self.assertEqual(is_package_support_py3(
            {'classifiers': ['Programming Language :: Python :: 3.3']}),
            True)

    def test_get_package_github_url(self):
        # github url found in pypi package data
        self.assertEqual(get_package_github_url(
            {'home_page': 'https://github.com/PythonCharmers/autoporter'}),
            'https://github.com/PythonCharmers/autoporter')

        self.assertEqual(get_package_github_url(
            {'home_page': 'http://github.com/PythonCharmers/autoporter'}),
            'http://github.com/PythonCharmers/autoporter')

        # github url not found, so check home_page
        urlopen = self.get_mock_urlopen('<html><a href="">abc</a><a>123</a><a href="http://www.google.com/about">ga</a></html>')
        with patch('utils.urlopen', MagicMock(return_value=urlopen)):
            self.assertEqual(get_package_github_url(
                {'home_page': 'http://www.google.com'}),
                None)

        urlopen = self.get_mock_urlopen('<html><a href="/about">abc</a><a href="https://github.com/PythonCharmers/autoporter">123</a></html>')
        with patch('utils.urlopen', MagicMock(return_value=urlopen)):
            self.assertEqual(get_package_github_url(
                {'home_page': 'http://www.google.com'}),
                'https://github.com/PythonCharmers/autoporter')

        urlopen = self.get_mock_urlopen('<html><a href="https://github.com/1/a">1a</a><a href="https://github.com/1/b">1b</a></html>')
        with patch('utils.urlopen', MagicMock(return_value=urlopen)):
            self.assertEqual(get_package_github_url(
                {'home_page': 'http://www.google.com'}),
                'https://github.com/1/a')

    def get_mock_urlopen(self, html):
        urlopen = MagicMock()
        urlopen.read = MagicMock()
        urlopen.read.return_value = html
        return urlopen


def main():
    '''A simple CLI script to test a package in PyPI.

    To run this script, do something like this in bash:
    $ PYTHONPATH=`pwd` python tests/test_package.py PACKAGE_NAME

    Replace PACKAGE_NAME with a package found in PyPI
    '''
    import sys
    package = sys.argv[1]

    package_data = get_pypi_package_data(package)
    if package_data is None:
        print('NO package data found for {}'.format(package))
        sys.exit(1)

    if is_package_support_py3(package_data):
        print('py3 OK')
        sys.exit(0)

    print('py3 NOT OK')

    # check if there is github page
    github_url = get_package_github_url(package_data)
    if github_url is None:
        print('github NOT FOUND')
        sys.exit(0)

    print('github FOUND {}'.format(github_url))

    sys.exit(1)


if __name__ == '__main__':
    main()
