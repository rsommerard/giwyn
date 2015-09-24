from git import *

class GitObj(object):

    def __init__(self, entry):
        self.entry = self.check_entry(entry)
        self.git_object = self.get_repo_from_entry(entry)
        self.current_status = self.return_current_status()
        self.all_commits = len(list(self.git_object.iter_commits()))
        self.commits_to_push = self.return_nb_commits_to_push()
        self.untracked_files = len(self.git_object.untracked_files)

    def __del__(self):
        pass

    def __str__(self):
        return "\t[{0}] {1} -- {2} commits -- {3} untracked files".format(self.current_status, self.entry, self.all_commits, self.untracked_files)

    def check_entry(self, entry):
        if entry[-1] == '\n':
            entry = entry[:-1]
        return entry

    def get_repo_from_entry(self, entry):
        return Repo(self.entry)

    def return_current_status(self):
        if self.git_object.is_dirty():
            return "DIRTY"
        elif not "Your branch is up-to-date" in self.git_object.git.status():
            return "TO PUSH"
        else:
            return "CLEAN"

    def return_nb_commits_to_push(self):
        return 0
