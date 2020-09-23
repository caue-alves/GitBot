import json
from os import system
from rich.console import Console
from rich import print
from dependencies import init

console = Console()

console.input("[bold magenta]Bem vindo ao GitBot!, digite enter para começar ...[/bold magenta]\n")

print("[bold cyan]Algum comando extra?([bold green]S[/bold green]/[bold red]N[/bold red])[/bold cyan]")
r = console.input("[bold blue]GitBot[/bold blue][bold magenta]> [/bold magenta]")
t = True
while t:
    if "S" in r.upper():
        print("[bold magenta]Insira o comando adicional:[bold magenta]")
        comando = console.input("[bold blue]GitBot[bold blue][bold magenta]> [/bold magenta]")
        if comando != "":
            t = False
    if "N" in r.upper():
        comando = "echo ."
        t = False

with open("infra/gbconfig.json", "r") as jj:
    f = json.load(jj)
    system(f'cd {f["path"]}')
    if f['first_time'] == "true":
        init()
        system("git init")
        system(f"git remote add origin {f['url']}")
        with open("infra/gbconfig.json", "w") as jf:
            dicio = {"path" : f["path"], "url" : f["url"], "first_time" : "false"}
            json.dump(dicio, jf, indent=4)
            with open('.gitignore', 'w') as git:
                git.write("/venv/\n/infra\n.idea")

    system('git add .')
    system(comando)
    system('git commit -m "GitBot Commit"')
    system(f'git push -u origin master')
    print("[bold green]OPERAÇÃO REALIZADA[/bold green]")