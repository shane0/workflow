#!/bin/bash
# https://shanenull.com/cheatsheets/macos/
# touch ~/.bash_profile
# touch ~/.bash_aliases
# source ~/.bash_profile
# todo fix macos  breaking path to code
# this failed to fix it
# where is it?
# which code
# /usr/local/bin/code
# /Users/shanenull/.cookiecutters/workflow
# export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"

# turn on vi mode
set -o vi
# turn off
# set -o emacs

# if [ -f ~/.bash_aliases ]; then
#     source ~/.bash_aliases
# fi


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

# nucamps docs suggest this they have tshooting docs they fail
# my time suck threshold was exceeded
# macos and nvm are
# export NVM_DIR="$HOME/.nvm"
# [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
# [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# install nvm
# curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash
# => nvm is already installed in /Users/shanenull/.nvm, trying to update using git
# failed this is tshooting
# exec $SHELL to reload shell
# source ~/.zshrc   # For Zsh
# source ~/.bash_profile   # For Bash
# echo $SHELL
# echo $NVM_DIR
# nvm --version
# command not found
# check or set permission should show your username
# ls -ld ~/.nvm
# whoami
# sudo chown -R yourusername:staff ~/.nvm
# cd ~/.nvm
# git pull origin master
# blah rebase git config pull.rebase true
# export NVM_DIR="$HOME/.nvm"
# [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
# [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" # This loads nvm bash_completion
# touch ~/.bash_aliases
# source ~/.bash_profile
# todo fix macos  breaking path to code
# this failed to fix it
# where is it?
# which code
# /usr/local/bin/code
# /Users/shanenull/.cookiecutters/workflow
# export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"



eval "$(/opt/homebrew/bin/brew shellenv)"
if command -v pyenv 1>/dev/null 2>&1; then
    eval "$(pyenv init -)"
    eval "$(pyenv init --path)"
fi


# nucamps docs suggest this they have tshooting docs they fail
# my time suck threshold was exceeded
# macos and nvm are
# export NVM_DIR="$HOME/.nvm"
# [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
# [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# install nvm
# curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash
# => nvm is already installed in /Users/shanenull/.nvm, trying to update using git
# failed this is tshooting
# exec $SHELL to reload shell
# source ~/.zshrc   # For Zsh
# source ~/.bash_profile   # For Bash
# echo $SHELL
# echo $NVM_DIR
# nvm --version
# command not found
# check or set permission should show your username
# ls -ld ~/.nvm
# whoami
# sudo chown -R yourusername:staff ~/.nvm
# cd ~/.nvm
# git pull origin master
# blah rebase git config pull.rebase true
# export NVM_DIR="$HOME/.nvm"
# [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
# [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" # This loads nvm bash_completion
