# Create my aliases
. ~/.alias.bash

# Git branch in prompt.
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\W\[\033[32m\]\$(parse_git_branch)\[\033[00m\] $ "

#let MC keep the path on exit
alias mc=". /usr/local/Cellar/midnight-commander/4.8.11/libexec/mc/mc-wrapper.sh"
