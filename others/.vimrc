"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"
" Update date : 2019/08/15
" Version : 2.0.0
"
" Last modified:
"	1. Trim contents in .vimrc file
"	 - Sort plugin list order alphabetically
"	 - Remove unnecessary comments
"	 - Move some settings from previous locations to their appropriate
"	 categories
"
"	2. Update plugins to their latest statuses
"
"	3. Remove all customized keymaps for jinja template syntax from
"	surround.vim
"
"	4. Remove keymap for manual flake8 checkings(cuase it's done
"	automatically after every file saving)
"
"
" * https://github.com/shoark7 *
" * All rights are not reserved *
" * Distribution is really appreciated.
"
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()


"""""""""""""""""""""""""""""""""""""""""""
"""""""""""""  Plugin lists  """"""""""""""
"""""""""""""""""""""""""""""""""""""""""""

Plugin 'altercation/vim-colors-solarized'
Plugin 'Emmet.vim'
Plugin 'git://git.wincent.com/command-t.git'
Plugin 'gmarik/Vundle.vim'
Plugin 'jnurmine/Zenburn'
Plugin 'kien/ctrlp.vim'
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
Plugin 'L9'
Plugin 'nvie/vim-flake8'
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
Plugin 'scrooloose/nerdcommenter'
Plugin 'scrooloose/syntastic'
Plugin 'snipMate'
Plugin 'srcexpl'
Plugin 'surround.vim'
Plugin 'taglist-plus'
Plugin 'The-NERD-Tree'
Plugin 'tmhedberg/SimpylFold'
Plugin 'tpope/vim-fugitive'
Plugin 'Valloric/YouCompleteMe'
Plugin 'vim-airline'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'Xuyuanp/nerdtree-git-plugin'

call vundle#end()


filetype plugin indent on


"""""""""""""""""""""""""""""""""""""""""""
"""""""""""  Basic settings  """"""""""""""
"""""""""""""""""""""""""""""""""""""""""""

set nocompatible
set encoding=utf-8
filetype off
set modifiable

set splitbelow
set splitright
set nu
set smartindent
set hlsearch
set ignorecase
set foldlevel=99
set foldmethod=indent
set noswapfile


"Set visual block copy yanked to global clipboard at v.1.7.3
set clipboard=unnamedplus  "For linux and vim over 7.3.74
"set clipboard=unnamed     "For macOS


"Indentation setting
""Indentaion setting for python
au BufNewFile,BufRead *.py,*.c
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set textwidth=100 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix

""Indentation for js, html, css
au BufNewFile,BufRead *.js,*.html,*.css
    \ set tabstop=2 |
    \ set softtabstop=2 |
    \ set shiftwidth=2 |


"Setting for whitespace
""Bad whitespace
"""Setting for BadWhitespace
highlight BadWhitespace ctermbg=red guibg=darkred

"""Notify for bad whitespaces"
au BufRead,BufNewFile,BufEnter *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

""whitespace for markdown at v.1.7.4
"""Setting for markdown whitespace
highlight NewlineWhitespace ctermbg=green guibg=green

"""Highlight newline character for markdown files.
au BufRead,BufNewFile,BufEnter *.md,*.markdown match NewlineWhitespace /\s\+$/


"Always open a file in a new tab
autocmd VimEnter * tab all


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


"Save and quit in insert mode. Same as Shift ZZ.
inoremap <S-Z>Z <ESC>:wq<CR>

"File Save in normal and insert mode.
"added at v1.1.5
nnoremap <S-F>S :w<CR>ma
inoremap <S-F>S <ESC>:w<CR>ma


"Key map for Emmet.vim
"" Keymap for expansion # 1.1.7
let g:user_emmet_expandabbr_key = '<c-e>'  " Which stands for 'e'mmet


"Key map for ctrlP
"Changed due to duplication with keymap for resizing window in vim at 1.6.3
let g:ctrlp_map = '<c-f>' " 'f' stands for 'find'


"Tab shifting with tab and <shift> + tab at v.1.7.0
""" tab goes to right and <shift> + tab goes to left
nnoremap <tab> :bnext<cr>
nnoremap <s-tab> :bprevious<cr>


"Key map for closing current buffer at v.1.7.1
nnoremap <leader>q :b#<bar>bd#<CR>
