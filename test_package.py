import caniusepython3 as ciu


def main():
    import sys
    project = sys.argv[1]
    result = ciu.check(projects=[project])
    print(result)

if __name__ == '__main__':
    main()
