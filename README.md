# xsquares

A tool for building perfectly square and rectangular crossword puzzles (called xsquares and xrectangles) from a word list.

# How it works

The program goes word by word in the word list, trying each one out at the first row. Then it looks for the 1st column, 2nd row, 2nd column, and so on until the nth row.

eg

T H A T

T H A T
H
I
S

# How to use

squares: ```python create_xsquare.py -n 5 --num 10` --start_index 0 --end_index 100```
rectangles: ```python create_xrectangle.py -w 5 -l --num 10` --start_index 0 --end_index 100```
    will search for 10 xsquares with rows and columns
    any of the arguments are optional

# Word lists

There are several options for long word lists, however you compromise between having many words and having normal english words. These can be found in the word_lists folder.

# Results

To see some of the sample outputs, look at the csv files in the outputs folder. Each row in the csv contains the rows of the xsquare.