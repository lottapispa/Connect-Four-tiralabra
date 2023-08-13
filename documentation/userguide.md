# User guide
### Commands
#### Installing dependencies
`poetry install`
#### Initialization:
`poetry run invoke build`
#### Starting game:
`poetry run invoke start`
#### Testing
`poetry run invoke test`
#### Test coverage report
`poetry run invoke coverage-report`
#### Pylint code review
`poetry run invoke lint`
### Instructions for playing:
-The goal of the game is to get four of your own pawns in a row horizontally, vertically or diagonally while preventing the other player from achieving the same. The first to connect four pawns wins. Since the rack is vertical rather than horizontal you can't put your pawns anywhere that's free. Instead, you have to drop them to the bottom of the rack or on top of other pawns. The gamerack is a matrix/nested list. So each list within the main list is a row. Last row is the bottom row (row 6). Pawn red will show on the rack as R and yellow as Y.  
<pre>
   1  2  3  4  5  6  7  
1 [0, 0, 0, 0, 0, 0, 0]  
2 [0, 0, 0, 0, 0, 0, 0]  
3 [0, 0, 0, 0, 0, 0, 0]  
4 [0, 0, 0, 0, 0, 0, 0]  
5 [0, 0, 0, 0, 0, 0, 0]  
6 [0, 0, 0, 0, 0, 0, 0]  
</pre> 
When starting the game, the program will ask you to choose a pawn color for yourself and if you want to start the game. The gamerack will be printed before your move. When it's asking for your move, it will first ask the row and then the column.  
##### Right now program still breaks after inputs!

