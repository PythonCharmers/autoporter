import caniusepython3 as ciu
from future.standard_library import hooks
with hooks():
    from urllib.parse import urlparse


def get_pypi_package_data(name):
    with ciu.pypi.pypi_client() as client:
        # get data for package
        releases = client.package_releases(name)
        if not releases:
            return None
        # just take the first one, for now
        version = releases[0]
        return client.package_data(name, version)


def is_package_support_py3(package_data):
    classifiers = package_data['classifiers']
    for classifier in classifiers:
        if 'Programming Language :: Python :: 3' in classifier:
            return True
    return False


def get_package_github_url(package_data):
    r = urlparse(package_data['home_page'])
    if r.netloc == 'github.com':
        return package_data['home_page']
    return None
