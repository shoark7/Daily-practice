"""""""""""""""""""""""""""""""""""""""""""
"
" Customized .vimrc file by Stonehead Park
" Last update Date : 2017/04/10
" Distribution is really appreciated.
" Version : 1.1.0
"
" Last modified:
"    1. Tab keymap added.
"	Moved on to tab oriented interface.
"	When you open a file, it is generally created in a new tab.
"	Now split is not the only option.
"	Tab related keymaps are below.
"    2. Others..
"    	Like prettifying the file,
"   	GotoDefinition of ycm is now okay.
"   	Fixed minor typos
"
" * https://github.com/shoark7 *
" * All rights are not reserved *
"
"""""""""""""""""""""""""""""""""""""""""""


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
let g:flake8_quickfix_location="topleft" "Setting for flake8

"ycm setting
let g:ycm_server_keep_logfiles = 1
let g:ycm_server_log_level = 'debug'
let g:ycm_autoclose_preview_window_after_completion=1
let g:ycm_goto_buffer_command = 'new-tab'

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

"Auto NERDTree option
"autocmd VimEnter * NERDTree
"autocmd BufEnter * NERDTreeMirror

"Folding option
set foldmethod=indent
set foldlevel=99

"Indentaion setting for python
au BufNewFile,BufRead *.py,*.c
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set textwidth=100 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix

"Indentation for js, html, css
au BufNewFile,BufRead *.js,*.html,*.css
    \ set tabstop=2 |
    \ set softtabstop=2 |
    \ set shiftwidth=2 |

"Notify for bad whitespaces"
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

"vim-flake8 checking
syntax on

"Theme toggling
call togglebg#map("<F5>")

"Always open a file in a new tab
autocmd VimEnter * tab all
"autocmd BufAdd * exe 'tablast | tabe "' . expand( "<afile") .'"'



"""""""""""""""""""""""""""""""""""""""""""
""""" Personally customized keymaps """""""
"""""""""""""""""""""""""""""""""""""""""""


"Useful shortcut 1. Shifting through windows
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

"Useful shortcut 2. fold and unfold
nnoremap <space> za

"Useful shortcut 3. ESC key --> jj
inoremap jj <ESC>

"Keymap for NERDTree and variable list toggle 
nmap <F8> :NERDTree<CR>
nmap <F9> :TlistToggle<CR>

"Keymap for window sizing
"Useful when using many windows at the same time
nmap <S-F5> :vertical resize +5<CR>
nmap <S-F6> :vertical resize -5<CR>
nmap <S-F7> :resize +5<CR>
nmap <S-F8> :resize -5<CR>

"Keymap for syntax inspection
"Python dedicated.
autocmd FileType python map <buffer> <F3> :call Flake8()<CR>

"Keymap for ENTER
map <Enter> i<ENTER>

"Go to definition keymap
nnoremap ff :YcmCompleter GoToDefinitionElseDeclaration<CR>

""" Tab keymaps.
"Creating and deleting a tab
nnoremap tn :tabnew<CR>
nnoremap tq :tabclose<CR>

"Keymap for tab shifting
nnoremap <F2> :tabprevious<CR>
nnoremap <F3> :tabnext<CR>

"Shifting through tabs with tab numbers.
nnoremap t1 1gt
nnoremap t2 2gt
nnoremap t3 3gt
nnoremap t4 4gt
nnoremap t5 5gt
nnoremap t6 6gt
nnoremap t7 7gt
nnoremap t8 8gt
nnoremap t9 9gt
nnoremap t0 10gt
"""
