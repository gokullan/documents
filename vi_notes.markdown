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

Commands

-   G -- last line

-   gg -- first line

-   To comment: Ctrl V + Shilf+I + '// ' + Esc (similar controls for
    uncommenting)

-   Copy (all contents) to clipboard: :%y+ or gg"+yG or gg"\*yG

    -   <https://superuser.com/questions/227385/how-do-i-select-all-text-in-vi-vim/1230483>
    -   <https://vim.fandom.com/wiki/Copy,_cut_and_paste>

-   Copy to system clipboard in visual mode

    -   Select text and type "+y

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

-   Disable preview

    -   <https://stackoverflow.com/questions/15962421/how-can-i-disable-scratch-preview-window>

-   Jump to matching brace: press \`%\`

-   Fix indentation: \`gg\`, then \`=G\`

    -   <https://www.freecodecamp.org/news/7-vim-tips-that-changed-my-life/>

-   [Using the Netrw File Explorer](https://vonheikemen.github.io/devlog/tools/using-netrw-vim-builtin-file-explorer/)
    -   `:Explore` to open the file explorer
    -   `-` to go one level up
    -   `mt` to mark a target directory
    -   `mf` to mark a file or directory
    -   `mm`, `mc`, ... to perform the required operation on the marked files/ directories (into the target directory)

**Misc**
-   Install `build-essential` and `libncurses-dev` before compiling vim from source
-   (**Important**) Compile vim with x-clip support
    -   [Commands for compilation](https://stackoverflow.com/questions/11416069/compile-vim-with-clipboard-and-xterm)
    -   [Specifying the necessary flags](https://superuser.com/questions/235505/compiling-vim-with-xterm-clipboard-support)
-   Backspace not working: Add `set backspace=indent,eol,start` to ~/.vimrc
-   Add clipboard functionality


**Plugins**
-   [Markdown Preview for Neo-vim](https://github.com/iamcco/markdown-preview.nvim)
-   Netrw (inbuilt with vim)
