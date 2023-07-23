# Project Requirements Specification

### Study program
Bachelor’s in computer science (CS)/Tietojenkäsittelytieteen kandidaatti (TKT)

### Project language
Python.

### Documentation and code language
English. I can do peer review in finnish as well.

### Algorithms and data structures
I'll be using minimax algorithm to create an AI player that other players can compete against. Alpha-beta-pruning will be used to make the minimax algorithm more efficient. The goal is to create an AI that is difficult as possible to defeat.

### Problem to be solved
Connect Four. The game has two players who compete against each other on a 6x7-sized rack that's used as a game board. The goal of the game is to get four of your own pawns in a row horizontally, vertically or diagonally while preventing the other player from achieving the same. The first to connect four pawns wins. The rack being vertical rather than horizontal makes the game more difficult since the players can't put their pawns anywhere. Instead, they drop them to the bottom of the rack or on top of other pawns.

### Program inputs
-

### Time- and space complexity
The goal is to achieve the worst-case performance $O(b^d)$ and the best-case performance ${\displaystyle O\left({\sqrt {b^{d}}}\right)}$ with alpha-beta-pruning.

### Sources
- "Connect Four", Wikipedia, wiki article, viewed 22 July 2023, https://en.wikipedia.org/wiki/Connect_Four
- "Minimax" 2023, Wikipedia, wiki article, viewed 22 July 2023, https://en.wikipedia.org/wiki/Minimax
- "Alpha-beta-pruning" 2023, Wikipedia, wiki article, viewed 22 July 2023, https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
- "Minimax-pelit", viewed 22 July 2023, https://tiralabra.github.io/2023_loppukesa/fi/aiheet/minimax.pdf
