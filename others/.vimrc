" Last update Date : 2018/03/01
" Distribution is really appreciated.
" Version : 1.7.3

" Last modified:
" 	1. Make visual block yank copied to the global clipboard
" 	 - If you now visually block + y, 
" 	   you can paste the content to othe programs.
"
"
" * https://github.com/shoark7 *
" * All rights are not reserved *
"
"""""""""""""""""""""""""""""""""""""""""""

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

"""""""""""""""""""""""""""""""""""""""""""
"""""""""""""  Plugin lists  """"""""""""""
"""""""""""""""""""""""""""""""""""""""""""

Plugin 'The-NERD-Tree'
Plugin 'taglist-plus'
Plugin 'snipMate'
Plugin 'srcexpl'
Plugin 'tmhedberg/SimpylFold'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'scrooloose/syntastic'
Plugin 'nvie/vim-flake8'
Plugin 'Valloric/YouCompleteMe'
Plugin 'jnurmine/Zenburn'
Plugin 'altercation/vim-colors-solarized'
Plugin 'kien/ctrlp.vim'
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
Plugin 'Emmet.vim'
Plugin 'surround.vim'
Plugin 'scrooloose/nerdcommenter'
Plugin 'Xuyuanp/nerdtree-git-plugin'
Plugin 'vim-airline' " At v.1.7.0
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




"""""""""""""""""""""""""""""""""""""""""""
"""""""""""  Basic settings  """"""""""""""
"""""""""""""""""""""""""""""""""""""""""""

set nocompatible              " be iMproved, required
set encoding=utf-8
filetype off                  " required
set modifiable

set splitbelow   "split directions
set splitright
set nu           " Number line generated when starting up vi
set smartindent  " Auto indenting when coding starts
set hlsearch     " Highlighted when search mode and normal mode
set ignorecase   " Ignorecase in search mode and normal mode
set foldlevel=99 "Folding options
set foldmethod=indent


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

"Setting for BadWhitespace
highlight BadWhitespace ctermbg=red guibg=darkred

"Notify for bad whitespaces"
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

"Always open a file in a new tab
autocmd VimEnter * tab all
"autocmd BufAdd * exe 'tablast | tabe "' . expand( "<afile") .'"'


"Non plugin settings after this line.
if has('gui_running')
	set background=dark
	colorscheme solarized
else
	colorscheme zenburn
	set background=dark
endif

"Theme toggling
""" Changed to f12 at v.1.6.4
call togglebg#map("<F12>")




"""""""""""""""""""""""""""""""""""""""""""
""""""""""""  Plugin settings  """"""""""""
"""""""""""""""""""""""""""""""""""""""""""

"Setting for NERDTREE
""" 1.5.0
let NERDTreeWinPos = "left"
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif
autocmd BufEnter * NERDTreeMirror  "All tabs share a one tree
let NERDTreeNaturalSort=1          "Files in trees are sorted in a natrual way, like 'z1.txt, z2.txt, z10.txt'
let NERDTreeMinimalUI = 1          "Minimal UI for NERDTREE
let NERDTreeShowHidden=1           "Set to show hidden files at nerdtree
""" Before 1.5.0
let g:NERDTreeWinSize=23  "Set default tree width from 31 to 23. Added at v.1.3.2
let Tlist_Ctags_Cmd = "/usr/bin/ctags"
let Tlist_Inc_Winwidth = 0
let Tlist_Exit_OnlyWindow = 0
let Tlist_Auto_Open = 0
let Tlist_Use_Right_Window = 1
let g:SimpylFold_docstring_preview=4 "Show simplyfold only one line
let python_highlight_all=1
let NERDTreeIgnore=['\.pyc$', '\~$', '\.git$'] "ignore files in NERDTree
let g:flake8_quickfix_location="topleft" "Setting for flake8


"Setting for ycm
let g:ycm_server_keep_logfiles = 0
let g:ycm_server_log_level = 'debug'
set completeopt-=preview  " Turn off preview window. It is annoying.. At 1.6.3
let g:ycm_goto_buffer_command = 'vertical-split'
let g:ycm_python_binary_path = '/home/sunghwanpark/.pyenv/versions/3.5.2/bin/python3.5' 
" This python route should have modules you want or ycm cannot suggest words or
" phrases you want


"Setting for vim-flake8
syntax on


"Setting for scroolose/nerdcommenter. At v.1.4.0
""" This plugin is a handy commenter for all languages
let g:NERDDefaultAlign = 'left'


"Setting for vim-airline at v.1.7.0
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#fnamemod = ':t'
let g:airline_section_b = '%{strftime("%c")}'
let g:airline_section_c = '%t'
"let g:airline_section_y = 'BN: %{bufnr("%")}'
let g:airline_section_error = ''
let g:airline_section_warning = ''
let g:airline_theme = 'badwolf'
set laststatus=2


"Setting for powerline
""" Install commands for poiwerline fonts
""" git clone https://github.com/powerline/fonts.git; cd fonts; ./install.sh

let g:Powerline_symbols = 'fancy'




"""""""""""""""""""""""""""""""""""""""""""
""""" Personally customized keymaps """""""
"""""""""""""""""""""""""""""""""""""""""""

"Useful shortcut 1. Shifting through windows - clockwise
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
""" Changed to f8, f9 at v.1.6.4
nmap <F8> :NERDTreeToggle<CR>
nmap <F9> :TlistToggle<CR>
"l keymap in vim not working in tmuxrdtree refresh keymap <Leader><r> at v.1.6.1
nmap <Leader>r :NERDTreeFocus<cr>R<c-w><c-p><esc> 


"Keymap for window sizing
""" Useful when using many windows at the same time
""" Changed to f3 ~ f6 at v.1.6.4
nnoremap <F3> :vertical resize +5<CR>
nnoremap <F4> :vertical resize -5<cr>
nnoremap <F5> :resize +5<cr>
nnoremap <F6> :resize -5<CR>


"Keymap for syntax inspection
""" Python dedicated.
""" changed to original keymap f7 at v.1.6.4
autocmd FileType python map <buffer> <F6> :call Flake8()<CR>


"Keymap for ENTER
map <ENTER> i<ENTER>


"Go to definition keymap
nnoremap fd :YcmCompleter GoToDefinitionElseDeclaration<CR>


" Tab keymaps.
""" Creating and deleting a tab
nnoremap tn :tabnew<CR>
nnoremap tq :tabclose<CR>


"Keymap for tab shifting
""" Changed to f1, f2 at v.1.6.4
nnoremap <F1> :tabprevious<CR>
nnoremap <F2> :tabnext<CR>
inoremap <F1> <ESC>:tabprevous<CR>
inoremap <F2> <ESC>:tabnext<CR>


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


"Save and quit in insert mode. Same as Shift ZZ.
inoremap <S-Z>Z <ESC>:wq<CR>

"File Save in normal and insert mode.
"added at v1.1.5
nnoremap <S-F>S :w<CR>ma
inoremap <S-F>S <ESC>:w<CR>ma


"Key map for Emmet.vim
"" Keymap for expansion # 1.1.7
let g:user_emmet_expandabbr_key = '<c-e>'  " Which stands for 'e'mmet


"Key map for surround.vim
""" Keymap for django jinja template # 1.2.0
let g:surround_{char2nr("b")} = "{% block '\r' %}\n{% endblock %}"
let g:surround_{char2nr("c")} = "{% comment \r %}\n\n{% endcomment %}"
let g:surround_{char2nr("f")} = "{% for \r %}\n\n{% endfor %}"
let g:surround_{char2nr("F")} = "{% for \r %}\n\n{% emtpy %}\n\n{% endfor %}"
let g:surround_{char2nr("i")} = "{% if \r %}\n\n{% else %}\n\n{% endif %}"
let g:surround_{char2nr("I")} = "{% if \r %}\n\n{% elif %}\n\n{% elif %}\n\n{% else %}\n\n{% endif %}"
let g:surround_{char2nr("p")} = "{% \r %}"


"Key map for ctrlP
"Changed due to duplication with keymap for resizing window in vim at 1.6.3
let g:ctrlp_map = '<c-f>'


"Tab shifting with tab and <shift> + tab at v.1.7.0
""" tab goes to right and <shift> + tab goes to left
nnoremap <tab> :bnext<cr>
nnoremap <s-tab> :bprevious<cr>


"Key map to close current buffer at v.1.7.0
""" This keymap closes current buffer with cursor on.
""" Becareful not to execute on NERDTree
""" <leader><q> exceutes the function
"function CloseCurrentBuffer()
"        let current_buffer=bufnr('$')
"        bn
"        exec 'bw'.string(current_buffer)
"endfunction

"nmap <Leader>q :call CloseCurrentBuffer()<CR>


"Key map for closing current buffer at v.1.7.1
""" My yesterday version was somewhat complex and I'll use simple one.
""" You know simple is better. Keymap is same
nnoremap <leader>q :b#<bar>bd#<CR>

"Set noswapfile at v.1.7.2
""" It was a big stress that vim makes swap files any time it's annoyed.
""" Stop that, boy.
set noswapfile


"Set visual block copy yanked to global clipboard at v.1.7.3
""" It was really annoying to copy vim contents and paste them into others.
""" This option lets visual block yank copyed to global clipboard
set clipboard=unnamedplus  "For linux and vim over 7.3.74
"set clipboard=unnamed     "For macOS
