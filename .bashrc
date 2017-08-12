#
# ~/.bashrc
#

if [ "$TERM" = "linux" ]; then
    clear
fi

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='\[\e[1;32m\][\u@\h \w]$\[\e[m\] '

alias wub='mpv --no-video --shuffle https://www.youtube.com/playlist?list=PLjgVd_07uAd95EmLlzcafgYjwIqHnIDUg'
alias yta="playerctl pause; mpv --no-video \"\$(xclip -selection clipboard -o)\"; playerctl play"

alias config='/usr/bin/git --git-dir=/home/dank/.cfg/ --work-tree=/home/dank'
