"Configuration for vi by Stonehead Park
"Date : 2016/12/24 Christmas-eve :)
"Distribution is really appreciated.
"Version : 1.0.2


set nocompatible              " be iMproved, required
set encoding=utf-8

filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
Plugin 'L9'
" Git plugin not hosted on GitHub
Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
" Plugin '/usr/share/vim/vim74/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Avoid a name conflict with L9
"Plugin 'user/L9', {'name': 'newL9'}

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ

"Plugin settings 
Plugin 'The-NERD-Tree'
Plugin 'AutoComplPop'
Plugin 'taglist-plus'
Plugin 'snipMate'
Plugin 'srcexpl'
Plugin 'tmhedberg/SimpylFold'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'scrooloose/syntastic'
Plugin 'nvie/vim-flake8'
Bundle 'Valloric/YouCompleteMe'
Plugin 'jnurmine/Zenburn'
Plugin 'altercation/vim-colors-solarized'
Plugin 'kien/ctrlp.vim'
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}

"Non plugin settings after this line.
if has('gui_running')
	set background=dark
	colorscheme solarized
else
	colorscheme zenburn
	set background=dark
endif

"Keymap for functions 
nmap <F8> :NERDTree<CR>
nmap <F9> :TlistToggle<CR>

"Keymap for window sizing
nmap <S-F5> :vertical resize +5<CR>
nmap <S-F6> :vertical resize -5<CR>
nmap <S-F7> :resize +5<CR>
nmap <S-F8> :resize -5<CR>

"Keymap for syntax inspection
autocmd FileType python map <buffer> <F3> :call Flake8()<CR>

"Keymap for personal utility
map <Enter> ko<ESC>i

"Window settings like positions of each window
let NERDTreeWinPos = "left"
let Tlist_Ctags_Cmd = "/usr/bin/ctags"
let Tlist_Inc_Winwidth = 0
let Tlist_Exit_OnlyWindow = 0
let Tlist_Auto_Open = 0
let Tlist_Use_Right_Window = 1
let g:SimpylFold_docstring_preview=4 "Show simplyfold only one line
let python_highlight_all=1
let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree
let g:flake8_quickfix_location="topleft" "Setting for flaek8
let g:ycm_server_keep_logfiles = 1
let g:ycm_server_log_level = 'debug'

"Setting for BadWhitespace
highlight BadWhitespace ctermbg=red guibg=darkred

"Which window to use when splitting off windows
set splitbelow
set splitright

" Number line generated when starting up vi
set nu

" Auto indenting when coding starts
set smartindent

" Highlighted when search mode and normal mode
set hlsearch

" Ignorecase in search mode and normal mode
set ignorecase

"Useful shortcut 1. Shifting through windowsa
    "Next window
nnoremap <C-W> <C-W><C-W>
    "Down window
nnoremap <C-J> <C-W><C-J>
    "Upper Window
nnoremap <C-K> <C-W><C-K>
    "Right window
nnoremap <C-L> <C-W><C-L>
    "Left window
nnoremap <C-H> <C-W><C-H>

"Useful shortcut 2. Making fold and unfold
nnoremap <space> za

"Useful shortcut 3. ESC key --> jj
inoremap jj <ESC>

"Auto NERDTree option
"autocmd VimEnter * NERDTree
"autocmd BufEnter * NERDTreeMirror

"Folding option
set foldmethod=indent
set foldlevel=99

"Indentaion setting for python
au BufNewFile,BufRead *.py
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set textwidth=100 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix

"Indentation for js, html, css
au BufNewFile,BufRead *.js, *.html, *.css
    \ set tabstop=2 |
    \ set softtabstop=2 |
    \ set shiftwidth=2 |

"Notify for bad whitespaces"
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

"vim-flake8 checking
syntax on

"Theme toggling
call togglebg#map("<F5>")
