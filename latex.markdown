Latex

-   Main reference: <https://en.wikibooks.org/wiki/LaTeX>

-   Inline equations: enclose in \$ \<\> \$

-   'Block' equations: enclose in \$\$ \<\> \$\$

-   \\pi, \\alpha, \\beta \...

-   Autoscale brackets: \\left, \\right

-   \\lim\_{n\\to\\infty}

-   \\frac{numerator}{denominator}

-   n^th^ root of x: \\sqrt\[n\]{x}

-   Summation from n=0 to infinity: \\sum\_{n=0}\^{infty}

-   Diagonal dots: \\ddots

-   Symbols
    -   Hadamard: \odot ($\odot$)
    -   Tilde on top: ~{x} ($\~{x}$)
    -   Hat (cap): \hat{x} ($\hat{x}$) 

-   Listing

    -   Numbered:

        \\begin{enumerate}

        -   \\item Item 1 \...

        \\end{enumerate}

    -   Bulleted:

        \\begin{itemize}

        -   \\item Item 1 \...

        \\end{itemize}

-   \\section{SectionName} (or) \\section\*{SectionName}

-   Integral a -\> b (f(x) dx) : int\_{a}\^{b}f(x)dx

- Piecewise functions:
  <https://tex.stackexchange.com/questions/32140/how-to-write-a-function-piecewise-with-bracket-outside>

  \\\[ \\begin{cases}

  -   0 & x\\leq 0 \\\\ \...

  \\end{cases} \\\]
  
    - Below uses arrays (can be used in Mattermost, Jupyter)
    - Reference [1](https://stackoverflow.com/questions/54281104/how-to-write-piecewise-function-in-jupyter-notebook-markdown)
    ```latex
    N(a) = \left\{
    \begin{array}{ll}
          n_o & A>A_{krit} \\
          n_o+2 & A=A_{krit} \\
          n_o+4 & A<A_{krit} \\
    \end{array} 
    \right.
    ```

-   <https://tex.stackexchange.com/questions/258192/how-can-i-make-a-math-version-of-itemize-enumerate-and-description-environment>

-   \\underset{below}{above}

    <https://stackoverflow.com/questions/6048661/how-to-place-a-character-below-a-function-in-latex>

-   Using superscript outside math mode - \\textsuperscript{}

-   Line breaks

    -   newline \\\\
    -   <https://tex.stackexchange.com/questions/208442/how-to-put-two-newlines-in-latex>

-   Alignment and Spacing

    -   space \~
    -   \\medskip or \\bigskip to give line break between ordinary
        paragraphs
    -   `\hspace{2mm}` for inline spacing (horizontal)
    -   `\hfill some content` pushes content to the right
    -   `\raggedright` and `\raggedleft` for left and right alignment respectively (?)

-   Custom commands
    ```latex
    \newcommand{\mycommand}[n] {  % n denotes the number of args to the command
        % use #i to access the ith argument 
    }
    ```

-   Parbox
    -   Below snippet to create a parbox with custom line-spacing
    ```latex
    \parbox{width}{\linespread{1.5}\selectfont ...}
    ```

-   Adding icons
    ```latex
    \usepackage{fontawesome5}
    \faGithub
    ```

-   `\textsuperscript{}` or `\textsubscript{}`

-   Latex Graphics
    -   [Tutorial](https://www.overleaf.com/learn/latex/LaTeX_Graphics_using_TikZ%3A_A_Tutorial_for_Beginners_(Part_1)%E2%80%94Basic_Drawing)
    
    -   Flowchart
        ```latex
        \documentclass{article}
        \usepackage{tikz}
        \usetikzlibrary{shapes.geometric, arrows}
        
        % use `tikzstyle` to pre-define styles for elements
        % \tikzstyle{element_name} = [... styles ...]
        \tikzstyle{process} = [rectangle, rounded corners, minimum width=3cm, minimum height=1cm, text centered, text width=3cm, draw=black, fill=orange!30]
        \tikzstyle{arrow} = [thick,->,>=stealth]
        
        \begin{document}
        
        % node `distance` refers to the distance between the centers of 2 (consecutive) nodes
        % `inner sep` and `outer sep` are analogous to padding and margin respectively
        \begin{tikzpicture} [node distance=3cm, style={inner sep=.5cm,outer sep=0}]
        % \node (node_name) [.. styles ..] {text_inside}
        \node (p1) [process, align=center] {MIMIC-IV ICU Admissions\\66239};
        \node (p2) [process, below of=p1, align=center] {Vitals \& Ventilator data present\\ \textbf{34143}};
        \node (p3) [process, below of=p2, align=center] {Age data present\\34143};
        \node (p4) [process, right of=p1, xshift=3cm, align=center] {Blood Gas Analysis present\\26073};
        \node (p5) [process, right of=p2, xshift=3cm, align=center] {Comorbidities present\\26073};
        \node (p6) [process, right of=p3, xshift=3cm, align=center] {Blood count present\\22609};
        
        \draw [arrow] (p1) -- (p2);
        #\draw [arrow] (p2) -- (p3);
        % arrow from p3 goes up; stops at 1cm left of p4 and extends to p4 horizonatally
        \draw [arrow] (p3) -| ([xshift=-1cm]p4.west) -- (p4.west);
        \draw [arrow] (p4) -- (p5);
        \draw [arrow] (p5) -- (p6);
        \end{tikzpicture}
        
        \end{document}
        ```
        -   Use `align=center` in node style to allow newlines in the textual content
        -   [Relative positioning of nodes using the `positioning` library](https://tex.stackexchange.com/questions/51228/how-to-increase-the-horizontal-distance-between-nodes)
        -   [Padding and margin for nodes](https://tex.stackexchange.com/questions/136391/tikz-remove-margin-padding-border-around-nodes-containing-images)
        -   Changing arrow-direction - [Example](https://tex.stackexchange.com/questions/388079/how-to-change-direction-of-arrow-tikz)

    -   Tikz
        -   [Manual](https://tikz.dev/tikz-shapes) (same as ~/Documents/latex/tikzpgfmanual.pdf)
        -   [Positioning Tikz pictures](https://tex.stackexchange.com/questions/123895/positioning-tikz-pictures)
        -   [Filling shapes with images](https://tex.stackexchange.com/questions/219356/how-to-create-a-rectangle-filled-with-image-using-tikz)

    -   Drawing shapes/ persons -- tikz

        -   Documentation: \~/Documents/VisualTikZ.pdf
        -   Wrapping text in node (text width) -
            <https://tex.stackexchange.com/questions/6899/tikz-multi-line-text-in-the-node-description>
        -   Captioning tikz picture --
            <https://tex.stackexchange.com/questions/24000/how-to-add-caption-for-a-tikz-picture>
        -   
        -   Note: If you want to place tikz images side by side, do not give
            a line break
        -   Checkmark --
            <https://tex.stackexchange.com/questions/132783/how-to-write-checkmark-in-latex>

-   Tables

    ```latex
    \usepackage{array}
    ...
    \begin{tabular}{|c|m{4cm}|}  % 2nd column should have a width of 4 cm with contents placed in the middle of each corresponding cell
        \hline
        cell 1 & \parbox{4cm}{This is the\\2nd cell\\I can choose the line breaks.}

    \end{tabular}
    ```
    -   Learn more [here](https://www.overleaf.com/learn/latex/Tables)
    -   Diagonal box --
        <https://tex.stackexchange.com/questions/27193/latex-table-cell-with-a-diagonal-line-and-2-sub-cells>

-   Graphs

    -   <https://tex.stackexchange.com/questions/57152/how-to-draw-graphs-in-latex>

- Monospace font
  - `\texttt{...}`
  - `\verb|...|`
  - Note: underscores need to be escaped

-   [Bibliography](https://www.overleaf.com/learn/latex/Bibliography_management_with_bibtex)
    -   [Converters](https://www.bibtex.com/converters/)
    -   [BibTex Tidy](https://flamingtempura.github.io/bibtex-tidy/)
