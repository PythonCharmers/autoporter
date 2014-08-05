import os
import subprocess

class Futurize:

    def modify_repo(self, local_path):
        print('futurize_forked_repo')
        for root, directories, files in os.walk(local_path):
            for file in files:
                if file.endswith((".py")):
                    subprocess.call(["futurize", "-w", "--nobackups", "--stage1", os.path.join(root, file)])