import gitapi

class Git():
    def __init__(self, github_credentials):
        self.github_credentials = github_credentials

    def clone_forked_repo(self, repo_url, local_path):
        print('clone_forked_repo')
        return gitapi.Repo.git_clone(repo_url, local_path)

    def add_changes(self, repo):
        print('git_add_changes')
        git_status = repo.git_status()
        for modified_file in git_status['M']:
            repo.git_add(modified_file)

    def commit_changes(self, repo):
        print('git_commit_changes')
        repo.git_commit("Committing changes made by futurize.", user=self.github_credentials['email'])

    def push_changes(self, repo, local_path):
        print('git_push_changes')
        repo.git_push()