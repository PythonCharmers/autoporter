from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from . import pypi_scanner


def main():
	scanner = pypi_scanner.pypi_scanner()
	github_packages = scanner.get_python2_github_packages()

if __name__ == '__main__':
	main()
