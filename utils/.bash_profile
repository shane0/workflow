#!/bin/bash
# touch ~/.bash_profile
# touch ~/.bash_aliases
# source ~/.bash_profile
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"



if [ -f ~/.bash_aliases ]; then
  source ~/.bash_aliases
fi


eval "$(/opt/homebrew/bin/brew shellenv)"
if command -v pyenv 1>/dev/null 2>&1; then
eval "$(pyenv init -)"
eval "$(pyenv init --path)"
fi

source_bash_functions() {
    local modules_dir="$HOME/.cookiecutters/workflow/utils/alias_files"
    if [ -d "$modules_dir" ]; then
        for file in "$modules_dir"/.bash_*; do
            echo sourcing $file
            [ -r "$file" ] && source "$file"
        done
    fi
}

source_bash_functions
