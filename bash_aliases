# bullet journaling aka bujo 
#set -o vi

# manage aliases
alias ea='vim ~/.bash_aliases'
alias sa='source ~/.bashrc'

# macos
alias c='clear'
alias r='ranger'
alias rd="vim ./readme.md"
alias cl="vim ./changelog.md"
alias jf='mkdir "$(date +%F)" && cd "$(date +%F)"'
alias ft='vim ./future.md'
alias in='vim ./index.md'
alias fj='vim ./"$(date +%F)".md'
alias bj='cd ./bujo && fj || echo "there is no bujo folder"'
alias bujo='cd ./bujo && fj || mkdir bujo && cd ./bujo && vim ./"$(date +%F)".md'

# git
alias grem='git ls-remote --heads | cut -d '/' -f 3'





# todocli app
alias t='clear && ./todocli/todo.sh'
alias d='clear && t listpri a'
alias snooze='clear && t listpri'
alias done='clear && cat ./todocli/done.txt'
alias tedit='vim ./todocli/todo.txt'
alias tall='clear && find . -name "todo.txt" | xargs grep "+"'
alias tpri='clear && find . -name "todo.txt" | xargs grep "(A"'
alias tprib='clear && find . -name "todo.txt" | xargs grep "(B"'
alias tpric='clear && find . -name "todo.txt" | xargs grep "(C"'
alias thelp='clear && ./todocli/todo.sh shorthelp'
