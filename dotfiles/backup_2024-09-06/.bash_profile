#!/bin/bash
# touch ~/.bash_profile
# touch ~/.bash_aliases
# source ~/.bash_profile

if [ -f ~/.bash_aliases ]; then
  source ~/.bash_aliases
fi


eval "$(/opt/homebrew/bin/brew shellenv)"
if command -v pyenv 1>/dev/null 2>&1; then
eval "$(pyenv init -)"
eval "$(pyenv init --path)"
fi
