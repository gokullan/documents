Vi notes

Shell Programming

-   Bash reference manual -
    <https://www.gnu.org/software/bash/manual/bash.html>
-   Giving permission -- chmod +x filename.sh

-   General

    -   **\$()** is used for enclosing commands; **\${} **is used for
        enclosing variables
    -   Command-line parameters are referred to as \$1, \$2, \..., \$n
    -   ***if \[ \]** *is different from ***if (( ))***
    -   \<\>

-   Which shell?

    -   Echo "\$SHELL"
    -   ps -p \$\$
    -   <https://www.freecodecamp.org/news/bash-array-how-to-declare-an-array-of-strings-in-a-bash-script/>

-   **while** loop

    -   <https://www.cyberciti.biz/faq/bash-while-loop/> (GOOD!)
    -   while \[ condition \]

do

\<some code\>

done

-   **for** loop

    -   <https://www.cyberciti.biz/faq/bash-for-loop/>
    -   for (( i=0; i\<\$n; ++i))

do

\<some code\>

done

-   -   for i in \$seq(( start inc. end ))

        -   seq LAST

seq FIRST LAST

seq FIRST INCREMENT LAST

-   -   for i in {start..end..inc}

        -   variables don't work inside?

-   Use ***bc*** for **floating-point arithmetic**

    -   echo "scale = 2; \$VAR1 + \$VAR2" \| bc -- l

    -   For more, see

        -   <https://stackoverflow.com/questions/12722095/how-do-i-use-floating-point-arithmetic-in-bash>

        -   <https://stackoverflow.com/questions/8654051/how-can-i-compare-two-floating-point-numbers-in-bash>

            -   See this for a note on using \`bc\` for exponents and
                with conditionals

-   Get **base**, **directory** and **file extension** names

    -   Get basename: *\${variableName##\*/}*
    -   For others, see
        <https://www.cyberciti.biz/faq/bash-get-basename-of-filename-or-directory-name/>

-   Get **file-size**

    -   FILESIZE=\$(stat -c%s "FILENAME")

        -   What does the \`c\` flag mean?
            <https://stackoverflow.com/questions/61999630/what-does-c-mean-in-this-linux-shell-command>

    -   For more, see
        <https://unix.stackexchange.com/questions/16640/how-can-i-get-the-size-of-a-file-in-a-bash-script>

-   **String concatenation**: "before\${varName}after"

-   Comments

    -   single line: \#
    -   multi-line: *\<\< comment_name *\... code to comment \....
        *comment name*

-   sum=\`expr \$sum + 1\`(**no spaces before and after '='**; LHS
    should not have \$)

-   while doesn't seem to work with expr for some reason

-   Arrays

    -   Inserting new values in array-

FACTORIAL+=(\$((i \* FACTORIAL\[i-1\])))

((FACTORIAL\[i\] = i \* FACTORIAL\[i-1\]))

-   -   Declaring, displaying -
        <https://www.freecodecamp.org/news/bash-array-how-to-declare-an-array-of-strings-in-a-bash-script/>
    -   Searching, find-and-replace -
        <https://www.geeksforgeeks.org/array-basics-shell-scripting-set-1/>

-   When should you use '\$' before variables?

-   \$() and \${} (Command and Parameter/variable substitution)

-   Concatenation of strings: s=\${s1}\${s2}

-   Replacing characters-

```{=html}
<!-- -->
```
-   -   <https://reactgo.com/bash-replace-characters-string/>
    -   <https://stackoverflow.com/questions/2871181/replacing-some-characters-in-a-string-with-another-character>
    -   <https://unix.stackexchange.com/questions/97582/how-to-find-and-replace-string-without-use-command-sed>

-   Splitting strings - <https://linuxhint.com/bash_split_examples/>

-   String to char array -
    <https://stackoverflow.com/questions/7578930/bash-split-string-into-character-array>

-   Indexing strings -
    <https://unix.stackexchange.com/questions/303960/index-a-string-in-bash>

-   (( )) vs. \[ \] vs. \[\[ \]\] ?

-   () vs. \$() vs. {} -
    <https://stackoverflow.com/questions/31255699/double-parenthesis-with-and-without-dollar/31255942>

-   When to use "" around a variable -
    <https://stackoverflow.com/questions/10067266/when-should-i-wrap-quotes-around-a-shell-variable>

i=1

echo \$i \>\> 1

i=i+1 (i is assigned string value 'i+1')

echo \$i \>\> i+1

WHAT OTHERS DON'T WORK?

i=\$i+1 \>\> 1+1

i=\${i+1} \>\> 1

WHAT IS CORRECT?

((i=i+1))

i=\`expr \$i + 1\`

<https://stackoverflow.com/questions/13111967/raise-to-the-power-in-shell>

<https://www.shellscript.sh/functions.html>

<https://www.shell-tips.com/bash/arrays/#how-to-check-if-a-bash-array-contains-a-value>

<https://linuxhint.com/use_expansions_shell_script/>

<https://tldp.org/LDP/abs/html/>

<https://askubuntu.com/questions/1208159/how-do-i-install-vim-gnome-on-ubuntu-19-10> -
Use *sudo apt install vim-gtk3 *instead of *vim-gnome* (to use +
register)

# Vim

-   G -- last line

-   gg -- first line

-   To comment: Ctrl V + Shilf+I + '// ' + Esc (similar controls for
    uncommenting)

## Copy-pasting

-   Copy to other registers (`+` and `*`)
    -   `"*y` to copy current line
    -   `n"*yy` to copy `n` lines
    -   `"*p` to paste
    -   Use the `+` register to copy to external (global?) clipboard; use `*` to
        copy-paste between different vim applications.
    -   [Reference](https://stackoverflow.com/questions/3961859/how-to-copy-to-clipboard-in-vim)

-   Copy (all contents) to clipboard: :%y+ or gg"+yG or gg"\*yG

    -   <https://superuser.com/questions/227385/how-do-i-select-all-text-in-vi-vim/1230483>
    -   <https://vim.fandom.com/wiki/Copy,_cut_and_paste>

-   Copy to system clipboard in visual mode

    -   Select text and type "+y

-   Copying to clipboard (if not complied with `xclip`)
    -   Install `xclip` (`sudo apt install xclip`)
    -   Yank the required lines: this will be stored in the `"0` register
    -   `:call system('xclip -sel clipboard', @0)`

-   Select all: ggVG or ggy\$

    -   Select and Copy: :%y
    -   Select and Delete: :%d
    -   <https://linuxtect.com/how-to-select-all-in-vim-vi/>
    -   Delete from current line: dG
    -   Delete from cursor-position: d Ctrl + End

-   Show special characters: set list (set no list)

-   Find and replace

    -   %s/to_replace/replacement/g
    -   if the expression to replace contains '.', use '\\.'

-   Remove special characters: %s/\^M//g

    -   <https://its.ucsc.edu/unix-timeshare/tutorials/clean-ctrl-m.html>

-   Remove lines starting with special characters: g/\^\$/d

    -   <https://stackoverflow.com/questions/706076/vim-delete-blank-lines>

    -   Regex

        -   <https://stackoverflow.com/questions/33022051/regex-explanation>
        -   <https://regex101.com/>

-   Find a pattern: /\<pattern\>

    -   Press n to go forward; N to go backward
    -   <https://www.cyberciti.biz/faq/find-a-word-in-vim-or-vi-text-editor/>

-   Set numbering for lines: set number or set nu (set nonumber or set
    nu!)

    -   <https://www.cyberciti.biz/faq/vi-show-line-numbers/>

-   Auto-indentation: set autoindent

    -   <https://developer.ibm.com/tutorials/au-vitips/>

-   To use mouse: `set mouse=a`

-   Character limit indicator: `set colorcolumn=80`

-   Wrapping
    -   `set textwidth=80` will ensure character-line limit *as* you type
    -   If this property is already set, but the line is not wrapped, go to
        visual mode and type `gq`

-   Disable preview

    -   <https://stackoverflow.com/questions/15962421/how-can-i-disable-scratch-preview-window>

-   Go to previous line: `Ctrl` + `O`
    -   For more related shortcuts, see [here](https://stackoverflow.com/questions/4837532/returning-to-previous-line-with-vim)

-   Jump to matching brace: press \`%\`

-   Fix indentation: \`gg\`, then \`=G\`

    -   <https://www.freecodecamp.org/news/7-vim-tips-that-changed-my-life/>

- Copy filename
  - [Reference](https://stackoverflow.com/a/64225287/13711617)
  ```
  " relative path
  :let @+ = expand("%")
  
  " full path
  :let @+ = expand("%:p")
  
  " just filename
  :let @+ = expand("%:t")
  ```

## Highlight
- `set hlsearch`
- `:noh` to turn off highlight until next search

## Windows, Tabs and Buffers
- [Tabs vs. Windows vs. Buffers](https://vi.stackexchange.com/questions/11072/is-it-possible-to-open-a-tab-in-a-window-and-not-a-window-in-a-tab)
- [Switching tabs](https://www.vimfromscratch.com/articles/vim-switching-tabs)
    -   `gt` or `gT` for sequential switching
    -   `xgt` or `xgT` or `:tabn x` to move to the tab number `x`
    -   `:tabmove x` to physically move the tab
    -   `wqa` or `qa` to close all tabs
- `:new filename` for a horizontal split; `:vert new filename` (OR) `vnew filename` for horizontal split
  - `set splitbelow` and `set splitright` to change default behaviour respectively
- To execute the currently open `.sh` file and redirect output to a vertical window, do `:vnew | read !bash #`
  - [Reference](https://superuser.com/a/868955/1653516)


-   [Using the Netrw File Explorer](https://vonheikemen.github.io/devlog/tools/using-netrw-vim-builtin-file-explorer/)
    -   `:Explore` to open the file explorer
    -   `-` to go one level up
    -   `mt` to mark a target directory
    -   `mf` to mark a file or directory
    -   `mm`, `mc`, ... to perform the required operation on the marked files/ directories (into the target directory)
    -   `d` to create a new directory
    -   `D` to delete a file or an empty directory
    -   `%` to create a new file
    -   `t` to open in a new tab
    -   Configuring
        -   [Set autonumbering](https://stackoverflow.com/questions/8730702/how-do-i-configure-vimrc-so-that-line-numbers-display-in-netrw-in-vim): Add `let g:netrw_bufsettings = 'noma nomod nu nobl nowrap ro'` to ~/.vimrc
    - For tree-view listing of directory, set `g:netrw_liststyle` to 3
    - [Quick Reference Guide](https://gist.github.com/t-mart/610795fcf7998559ea80)

-   [Vundle Plugin Manager]
    -   [Tutorial](https://linuxhint.com/vim-vundle-tutorial/)       
    -   [`PluginSearch` error](https://github.com/VundleVim/Vundle.vim/issues/599) 

- vim-plug 
  - In the installation instruction provided, the line
    `${XDG_DATA_HOME:-$HOME/.local/share}` may cause issues

-  YouCompleteMe
   -   [JS
       Autocomplete](https://blog.priDsmatik.com.au/snippets-in-vim-43cf2ad79000)

- Conquer of Completion (`coc.nvim`)
  - Use vim-plug and the `release` branch
  - Update Node path if needed (`g:coc_node_path`)
  - [List of extensions](https://github.com/neoclide/coc.nvim/wiki/Using-coc-extensions#implemented-coc-extensions) 
  - For key mappings in lua, see [here](https://github.com/neoclide/coc.nvim/discussions/3776)
  - `coc-format-json` for JSON fomatting. (`:CocCommand formatJson`)

-  Viewing Variables
   -    `:set all`
   -    [Variables associated with a plugin](https://stackoverflow.com/questions/62943877/how-to-view-all-variables-associated-with-a-plugin-in-vim)
   - `echo g:variable_name` to view a specific variable

## Key Bindings
- `<C-R>` - Carriage-Return
- `<Leader>` - `\` key by default

## Debugging
- [Using vimspetor](https://dev.to/iggredible/debugging-in-vim-with-vimspector-4n0m)
  - `pip3 install pynvim`
  - For NodeJS, use the gadget `vscode-js-debug`
- [Using vim-dap (and vim-dap-ui)](https://miguelcrespo.co/posts/how-to-debug-like-a-pro-using-neovim/)
  - It may be required to patch/ change the terminal font to render icons for vim-dap-ui
  - See `linux_commands.markdown` and [this link](https://github.com/rcarriga/nvim-dap-ui/issues/257).
- Use `persisted-breakpoints.nvim` for breakpoints-persistance. Check [this](https://github.com/mfussenegger/nvim-dap/issues/198) issue for more details.

## Lua
- `:lua print(vim.inspect(vim.api.nvim_list_runtime_paths()))` to view runtimepaths
### References
- [Lua guide - neovim](https://neovim.io/doc/user/lua-guide.html)
- [Using VimPlug with Lua](https://dev.to/vonheikemen/neovim-using-vim-plug-in-lua-3oom)
- [Neovim config sample - 1](https://github.com/miltonllera/neovim-config)
- [Ujjwaleshwar's config](https://github.com/Ujs113/nvim-config/tree/main)

**Misc**
-   Install `build-essential` and `libncurses-dev` before compiling vim from source
-   ❗️(**Important**) Compile vim with x-clip support
    -   [Commands for compilation](https://stackoverflow.com/questions/11416069/compile-vim-with-clipboard-and-xterm)
    -   [Specifying the necessary flags](https://superuser.com/questions/235505/compiling-vim-with-xterm-clipboard-support)
-   Refer [this link](https://github.com/ycm-core/YouCompleteMe/wiki/Building-Vim-from-source) to compile vim from source so that it is compatible with YouCompleteMe
-   Backspace not working: Add `set backspace=indent,eol,start` to ~/.vimrc


**Plugins**
-   [Markdown Preview for Neo-vim](https://github.com/iamcco/markdown-preview.nvim)
    -   For emojis, refer [here](https://www.webfx.com/tools/emoji-cheat-sheet/)
        for unicodes and
        [here](https://stackoverflow.com/questions/34538879/unicode-emojis-in-github-markdown)
        for the markdown syntax
-   Netrw (inbuilt with vim)
- [VimAwesome](https://vimawesome.com/) for plugin documentation

## Add comments/ answers
- [Can't open /tmp/...](https://stackoverflow.com/q/19697710/13711617)
