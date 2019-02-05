# Latex Table Generator
## What is this?
This small and compact python script will generate a table formatted by latex for use in latex editors such as __TexMaker__.

## Why not just write my table myself?
If you've ever tried to create a table with many inputs, it gets extremely tiring and confusing as you have to manually write & everytime and ensure everything is formatted correctly. This script aims to remove this pain and have a nice and easy way to create tables in latex!

Additionally, most people normally read a column vertically and users who don't need to look at their keyboard are able to input values in a straightforward way.
For example,

| p | q | p or q |
|:-:|---|--------|
| T | T | T      |
| T | F | T      |
| F | T | T      |
| F | F | F      |

Inputting this in Latex will result in entering values left to right separated by an ampersand, the first row entry would be T & T & T.

Now imagine this more than 3 columns and a lot of rows, it is incredibly tedious and prone to error.

With this script, you can enter one single column, the input for the first column would be T **__hit enter__** T **__hit enter__** F **__hit enter__** F **__hit enter__**.

This is much easier to keep up with for multiple values.

This program also automatically pads your columns as well, so for values that are varying widths such as **2381** compared to **21**, it has varying widths which makes the columns not equal size without manually padding it. This makes the raw Latex table easier to read and proofread.

## What are some features?
For now only the Truth Table is supported, there is more customizable tables coming for sure.

**Example of A Generated Truth Table**
<<<<<<< HEAD

    \begin{displaymath}
    \begin{array}{|c|c|c|}
    p        & q        & p \lor q \\
    \hline
    T        & T        & T        \\
    T        & F        & T        \\
    F        & T        & T        \\
    F        & F        & F        \\
    \end{array}
    \end{displaymath}

=======
```latex
\begin{displaymath}
\begin{array}{|c|c|c|}
p        & q        & p \lor q \\
\hline
T        & T        & T        \\
T        & F        & T        \\
F        & T        & T        \\
F        & F        & F        \\
\end{array}
\end{displaymath}
```
Note how the columns are properly spaced and easy to read even when its raw Latex!
