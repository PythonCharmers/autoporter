from githubpy.github import GitHub

class Github:

    def __init__(self, github_credentials):
        self.github = GitHub(github_credentials['name'], github_credentials['password'])

    # https://developer.github.com/v3/repos/forks/#create-a-fork
    def fork_repo(self, repository):
        print('fork_github_repo')
        return self.github.repos(repository['owner'])(repository['name']).forks.post()