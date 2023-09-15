#!/usr/bin/env bash

# pick your options 

# failover if you do not want to install cookiecutter
commands=(
    "echo mkdocs"
    "echo update the port number in the mkdocs and vscode task"
    "mkdocs new ."
    "rm mkdocs.yml"
    "cp ~/template/mkdocs.yml ."
    "> docs/index.md"
    "echo "[TAGS]" >> docs/index.md"
    "mkdir docs/images"
    "mkdir includes"
    "mkdir .vscode"
    "cp ~/template/.vscode/mkdocs.json .vscode/"
    "echo todocli"
    "cp ~/template/docs/todocli.md docs/"
    "cp -R ~/template/todocli/ ."
    "echo click"
    "$HOME/template/deploy.sh"
    "echo update upload.sh"
)

# Iterate over the list of commands
for command in "${commands[@]}"; do
    # Prompt the user if they want to run the command
    echo "run '$command'? (y/n)"
    read -r -n 1 response
    
    # If the user says yes, run the command
    if [[ $response == "y" ]]; then
        echo "Running '$command'"
        eval "$command"
    fi
done
