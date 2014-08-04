from urllib.parse import urlparse

import caniusepython3 as ciu


def main():
    import sys
    project = sys.argv[1]

    # check if there is github page
    with ciu.pypi.pypi_client() as client:
        releases = client.package_releases(project)
        if not releases:
            print('NO releases found for {}'.format(project))
            sys.exit(1)

        got_github = False
        version = releases[0]
        package_data = client.package_data(project, version)

        classifiers = package_data['classifiers']
        for classifier in classifiers:
            if 'Programming Language :: Python :: 3' in classifier:
                print('py3 OK')
                sys.exit(0)

        r = urlparse(package_data['home_page'])
        if r.netloc == 'github.com':
            got_github = True
        if got_github:
            print('github FOUND')
        else:
            print('github NOT FOUND')

    print('py3 NOT OK')
    sys.exit(1)

if __name__ == '__main__':
    main()
