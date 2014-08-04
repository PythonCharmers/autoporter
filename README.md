autoporter: Porting the universe to Python 2&3
==============================================

Tool to automate porting of Python 2-only packages to both Python 2&amp;3 and sending pull requests

https://github.com/PythonCharmers/autoporter

Vision:
-------
Automate porting of Py2 packages to Py3 while preserving compatibility with Py2.

Goal 1:
-------
write a script that takes a package name as an argument and does this:

1. Py3?: Examines whether it already has the Python 3 (or 3.3 or 3.4) trove classifier. If so, exit.

2. GitHub?: Examines whether there is a github link on the PyPI page. If not, exit.

3. Env: Creates a virtualenv for the package

4. Fork: Forks the package repo on GitHub

5. Clone: Clones the package to the local filesystem

6. Futurize: Runs futurize --stage1 on the code

7. Commit: Commits the changes locally

8. Test: If the package has a test suite, try running it with ``python setup.py test``.

8. Push: Pushes the changes to the new GitHub repo

9. PR: Sends a pull request (marked "Work In Progress") upstream


Goal 2:
-------
Run this script over all 47,000 packages on PyPI! :)

We can run this from e.g. an EC2 or Digital Ocean instance that has an SSD disk and is geographically close to the PyPI server.


People:
-------

- Ed Schofield <ed@pythoncharmers.com> (@edschofield)

- Ben Clews <bennett.clews@gmail.com> (@bennett_clews)

- James Berry <jmsbrry@gmail.com>

- Charles Prosper <charles_prosper@hotmail.com>

- Kevin Chen <mr.kevin.chen811@gmail.com>

- Simon Quach <simon.quach@butterfly.com.au>

- Luoxi Pan <l.panpax@gmail.com>

- Chee Ming <cheeming@gmail.com> (@cheeming)


Tools:
------

- Githubpy: http://github.liaoxuefeng.com/githubpy/

- Caniusepython3: https://github.com/brettcannon/caniusepython3

This has routines we can use to extract Trove classifiers (whether a package supports Py3 etc.)

- futurize: http://python-future.org:
```
    $ pip install future
    $ futurize --stage1 *.py
```
- Miniconda Python distribution (Ed's recommendation for easily creating side-by-side Py2 and Py3 environments): http://conda.pydata.org/miniconda.html


Notes:
------

- This will require packages to set Python 2.6 as their minimum supported version.

