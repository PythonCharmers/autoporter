#!/usr/local/bin/python
import argparse
import yaml
import os
from src.git import Git
from src.github import Github 
from src.futurize import Futurize

def main():
    parser = argparse.ArgumentParser(description='Futurize github repositories.')
    parser.add_argument('--github-repositories', help='Configuration file containing list of github repositories to futurize.', required=True)
    parser.add_argument('--github-credentials', help='Configuration file containing github credentials.', required=True)
    parser.add_argument('--local-repository-directory', help='Local directory used to store and modify github repositories.', required=True)
    args = parser.parse_args()

    stream = open(args.github_repositories, 'r')
    github_repositories = yaml.load(stream)

    stream = open(args.github_credentials, 'r')
    github_credentials = yaml.load(stream) 

    github = Github(github_credentials)
    git = Git(github_credentials)
    futurize = Futurize()

    for repository in github_repositories['repositories']:
        local_path = os.path.join(args.local_repository_directory, repository['name'])

        fork = github.fork_repo(repository)
        forked_repository = git.clone_forked_repo(fork['ssh_url'], local_path)

        futurize.modify_repo(local_path)
        
        git.add_changes(forked_repository)
        git.commit_changes(forked_repository)
        git.push_changes(forked_repository, local_path)

if __name__ == "__main__":
    main()
