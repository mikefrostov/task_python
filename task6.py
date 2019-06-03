#!/usr/bin/python



# Algorithm: iterate from first to last commit and check json syntax
# 0) get path to a repo as an argument from a cli
# 1) fetch first commit
# 2) check json files for corrupt file
# 3) if found return result
# 4) if all correct -> move to the next commit

import os
import subprocess
import json 
import sys
from git import Repo
from git import Git

def is_json(data):
    try:
        json_object = json.loads(data)
    except ValueError, e:
        print(str(e))
        return False
    return True


def traverse_commits(path):
    g = Git(path) # to checkout commits later   
    repo = Repo(path)  # get commit objects 
    commits = repo.iter_commits(paths=path)  
    commits_list = list(commits) 
    commits_list.reverse() #go first commit to last

    for commit in commits_list: #check each commit
        g.checkout(commit)
        json_files = [ x for x in os.listdir(path) if x.endswith(".json") ] 
        for json_file in json_files:
            fullpath = path + "/"+  str(json_file) #abs path to open file
            with open(fullpath) as f:  
                data = f.read()
                result = is_json(data)
                if not result:
                    print("Problemmatic commit is " + str(commit))
                    print("Problemmatic file is " + str(json_file))  
                    print("---------------") 
                    sys.exit(-1) 
    repo.heads.master.checkout() #reattach HEAD back to master

def main():
    
    cwd = os.getcwd()
    path = str(os.getcwd()) + "/examplerepo"
    traverse_commits(path)
    print("done")



if __name__ == '__main__':
    main()


