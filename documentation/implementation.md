# Implementation document

### Project Structure
```mermaid
classDiagram
    GameLoop ..> GameStatus
    GameLoop ..> GameRack
    GameLoop ..> Minimax
    GameStatus ..> GameRack
    Minimax ..> GameStatus
    Minimax ..> GameRack
    class GameLoop{
        +reference to GameStatus()
        +reference to GameRack()
        +reference to Minimax()
        +str who_starts
        +bool turn
    }
    class GameStatus{
        +reference to list gamerack
        +reference to int rows
        +reference to int columns
        +bool over
        +str winner
        +int status
        +check_for_win_hor()
        +check_for_win_ver()
        +check_for_win_dia()
        +is_game_over()
    }
    class GameRack{
        +int rows
        +int columns
        +list gamerack
        +str players_color
        +str ai_color
        +insert_piece()
        +next_move()
        +print_rack()
    }
    class Minimax{
        +reference to GameRack()
        +reference to GameStatus()
        +minimax()
    }
```

### Complexity 
| **file** | **time**
| --------- | ----------- 
| gameloop.py | 
| minimax.py |
| gamestatus.py | 
| gamerack.py |

### Improvements
Alpha-beta-pruning is not used yet.

### Sources
- "Connect Four", Wikipedia, wiki article, viewed 22 July 2023, https://en.wikipedia.org/wiki/Connect_Four
- "Minimax" 2023, Wikipedia, wiki article, viewed 22 July 2023, https://en.wikipedia.org/wiki/Minimax
- "Alpha-beta-pruning" 2023, Wikipedia, wiki article, viewed 22 July 2023, https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
- "Minimax-pelit", viewed 22 July 2023, https://tiralabra.github.io/2023_loppukesa/fi/aiheet/minimax.pdf
