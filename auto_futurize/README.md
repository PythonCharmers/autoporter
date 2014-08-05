auto_futurize
=============

This application performs the following steps:

1. Forks a github repository
2. Clones the forked github repository
3. Runs the futurize script over the cloned repository
4. Git adds the changes back into the repository
5. Commits the changes to the repository
6. Pushes the changes back into the forked github repository.

Note: I'm not sending through a pull request yet. Thought I'd wait until the code is a bit better.

Running the application
=======================

This is a command line application, which is run with the following required parameters:
- github-repositories: Configuration file containing list of github repositories to futurize.
- github-credentials: Configuration file containing github credentials.
- local-repository-directory: Local directory used to store and modify github repositories.

Configuration Files
===================

Configuration files are stored in YAML files. Examples can be found in the configuration folder.

Example
=======

Below is an example of how I'm running this application:

    python main.py --github-repositories=configuration/github_repositories.yaml --github-credentials=configuration/github_credentials.yaml --local-repository-directory=/Users/bclews/Projects/python_future_github/cloned_packages

TODO
====
- Unit tests! I've been slack during this hackathon...
- Remove repository folder once changes have been pushed back into forked github repository
