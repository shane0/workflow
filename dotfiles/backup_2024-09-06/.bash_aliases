# alias ea='vi ~/.bash_aliases'
alias ea='code ~/.bash_aliases'
alias sa='source ~/.bash_aliases'
alias c='clear'

alias vvv='set -o vi'
alias eee='set -o emacs'
alias fff='open https://github.com/shane0/workflow/issues/23' 
alias fffn='open https://learn.nucamp.co/mod/book/view.php?id=4895&chapterid=5067'
alias stt='set -o | grep vi'


alias fff='open https://github.com/shane0/workflow/issues/23'
alias day='date +%D && date +%j && date +%A && date +%d && date +%u'
alias mday='vim ./"$(date +%j)".md'
alias fj='vim ./"$(date +%F)".md'
alias fday='mkdir "$(date +%j)" && cd "$(date +%j)"'
# alias week='date +%V'
alias month='date +%B && date +%m'
alias year='date +%Y'


# Function to show the current shell
function show_terminal {
    echo "Current shell: $SHELL"
}

# Function to set shell to zsh
function set_zsh {
    echo "Setting shell to zsh..."
    chsh -s /bin/zsh
    echo "Please log out and log back in for changes to take effect."
}

# Function to set shell to bash
function set_bash {
    echo "Setting shell to bash..."
    chsh -s /bin/bash
    echo "Please log out and log back in for changes to take effect."
}

# Aliases to call the functions
alias ttt='show_terminal'
# alias zzz='set_zsh'
alias bbb='set_bash'

# Define a function to calculate the remaining weeks and print a progress bar
print_progress_bar() {
    local current_week=$(date +%U | sed 's/^0*//')
    local total_weeks=52
    local remaining=$((total_weeks - current_week))
    local percentage=$(( (current_week * 100) / total_weeks ))

    # Print progress bar
    local i
    local progress=""
    for ((i = 0; i < percentage / 2; i++)); do
        progress+="▓"
    done
    for ((i = percentage / 2; i < 50; i++)); do
        progress+="░"
    done

    echo "Week $current_week of $total_weeks"
    echo "Progress: [$progress] $percentage%"
}

# Alias to display the progress bar
alias week='print_progress_bar'

# homebrew requires xcode and bash
alias ixx='xcode-select --install'
alias ihh='/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
# (echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/shanenull/.bash_profile
# eval "$(/opt/homebrew/bin/brew shellenv)"
alias igg='brew install git'
# https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
# git config --global user.name "shane0"
# git config --global user.email "noreply@example.com"
# ssh-keygen -t ed25519 -C "noreply@example.com"
# eval "$(ssh-agent -s)"
# Host github.com
#   AddKeysToAgent yes
#   UseKeychain yes
#   IdentityFile ~/.ssh/id_ed25519
# ssh-add --apple-use-keychain ~/.ssh/id_ed25519
# touch ~/.ssh/config
# pbcopy < ~/.ssh/id_ed25519.pub
# ssh -T git@github.com
# git clone git@github.com:shane0/workflow.git
# brew install pyenv
# pyenv -v
# echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\neval "$(pyenv init -)"\neval "$(pyenv init --path)"\nfi' >> ~/.bash_profile
# source ~/.bash_profile
# pyenv install 3.9.9
# pyenv global 3.9.9
# python -V
# Set the backup folder path in a variable
# /Users/shanenull/workflow
# Define the function to back up files
backup_files() {
    # Get the current date in ISO format
    local date=$(date +%F)  # This produces yyyy-mm-dd
    
    # Define the backup folder with the date
    local backup_folder="$HOME/workflow/dotfiles/backup_$date"

    # Create the backup folder if it does not exist
    mkdir -p "$backup_folder"

    # Define the list of files to back up
    local files=(
        "$HOME/.bash_profile"
        "$HOME/.bash_aliases"
        # Add other files you want to back up here
    )

    # Back up each file
    for file in "${files[@]}"; do
        if [[ -f "$file" ]]; then
            cp "$file" "$backup_folder"
            echo "Backed up $file to $backup_folder"
        else
            echo "$file does not exist"
        fi
    done
}

# Create an alias to call the function
alias bbb='backup_files'
