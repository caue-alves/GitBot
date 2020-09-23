import json
from os import system

with open("infra/gbconfig.json", "r") as jj:
    f = json.load(jj)
    system(f'cd {f["path"]}')
    if f['first_time'] == "true":
        system("git init")
        system(f"git remote add origin {f['url']}")
        with open("infra/gbconfig.json", "w") as jf:
            dicio = {"path" : f["path"], "url" : f["url"], "first_time" : "false"}
            json.dump(dicio, jf, indent=4)
    system('git add .')
    system('git commit -m "GitBot Commit"')
    system(f'git push -u origin master')