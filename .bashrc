#
# ~/.bashrc
#

if [ "$TERM" = "linux" ]; then
    clear
fi

# If not running interactively, don't do anything
[[ $- != *i* ]] && return
[[ -f ~/.bash_profile ]] && . ~/.bash_profile

alias ls='ls --color=auto'
PS1='\[\e[1;32m\][\u@\h \w]$\[\e[m\] '

export VISUAL="nano"
export QT_QPA_PLATFORMTHEME="qt5ct"

alias wub='mpv --no-video --shuffle https://www.youtube.com/playlist?list=PLjgVd_07uAd95EmLlzcafgYjwIqHnIDUg'
alias mpvc="mpv --no-video \$(xclip -selection clipboard -o)"
alias mpva="mpv --no-video "

alias config='/usr/bin/git --git-dir=/home/dank/.cfg/ --work-tree=/home/dank'
