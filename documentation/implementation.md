# Implementation document

### Project Structure
```mermaid
classDiagram
    GameLoop ..> GameStatus
    GameLoop ..> GameRack
    GameLoop ..> Minimax
    GameLoop ..> Gamerack
    GameStatus ..> Gamerack
    Minimax ..> Gamerack
    class GameLoop{
        +str who_starts
        +str players_color
        +str ai_color
        +bool turn
    }
    class GameStatus{
        +list gamerack
        +int rows
        +int columns
        +bool over
        +bool turn
        +check_for_win_hor()
        +check_for_win_ver()
        +check_for_win_dia()
        +is_game_over()
    }
    class GameRack{
        +int rows
        +int columns
        +list gamerack
        +insert_piece()
        +next_move()
    }
    class Minimax{
        +minimax()
        +main()
    }
```

### Complexity 

### Improvements
Alpha-beta-pruning is not used yet.

### Sources
- "Connect Four", Wikipedia, wiki article, viewed 22 July 2023, https://en.wikipedia.org/wiki/Connect_Four
- "Minimax" 2023, Wikipedia, wiki article, viewed 22 July 2023, https://en.wikipedia.org/wiki/Minimax
- "Alpha-beta-pruning" 2023, Wikipedia, wiki article, viewed 22 July 2023, https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
- "Minimax-pelit", viewed 22 July 2023, https://tiralabra.github.io/2023_loppukesa/fi/aiheet/minimax.pdf
