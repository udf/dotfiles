call plug#begin('~/.local/share/nvim/plugged')
Plug 'chriskempson/base16-vim'
call plug#end()

" Map the leader key to SPACE
let mapleader="\<SPACE>"

set showmatch
set matchtime=0
set number
set formatoptions+=o
set expandtab
set tabstop=4
set shiftwidth=4

set nojoinspaces
set scrolloff=3
set sidescrolloff=5
set nostartofline

set mouse=a

" %s options
set ignorecase
set smartcase
set gdefault
" ctrl+l to clear search highligting
nnoremap <silent> <C-L> :nohlsearch<CR><C-L>
nmap <Leader>s :%s//g<Left><Left>

syntax enable
set synmaxcol=1024
set background=dark
let base16colorspace=256
colorscheme base16-default-dark
hi Comment ctermfg=20 cterm=italic
hi Normal ctermbg=NONE

