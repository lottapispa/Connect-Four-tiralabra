# Implementation document

### Project Structure
```mermaid
classDiagram
    GameLoop ..> GameStatus
    GameLoop ..> GameRack
    GameLoop ..> Minimax
    GameLoop ..> Score
    GameStatus ..> GameRack
    Minimax ..> GameStatus
    Minimax ..> GameRack
    Minimax ..> Score
    class GameLoop{
        +list rack
        +reference to GameStatus
        +reference to GameRack
        +reference to Minimax
        +str who_starts
        +bool turn
        +int depth
        +start_inputs()
        +main()
        +players_move()
        +end_prints()
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
        +str players_color
        +str ai_color
        +insert_piece()
        +next_move()
        +print_rack()
    }
    class Minimax{
        +reference to GameRack
        +reference to GameStatus
        +minimax()
        +choose_best_move()
    }
    class Score{
        +reference to GameRack
        +reference to GameStatus
        +heuristic_value()
        +score_for_moves()
    }
```

### Time complexity 
The time it takes to call choose_best_move in main loop with different ways to make a copy of the rack.
| **move** | **deepcopy** | **json** | **shallow copy in for loop** | **move** | **deepcopy** | **json** | **shallow copy in for loop**
| --------- | ----------- | -------- | ---------------------------- | -------- | ------------ | -------- | -------------------- 
| 4 | 0.486... s | 0.423... s | 0.384... s | 4 | 0.483... s | 0.427... s | 0.392... s
| 3 | 0.833... s | 0.739... s | 0.645... s | 5 | 0.739... s | 0.648... s | 0.596... s 
| 2 | 0.943... s | 0.828... s | 0.756... s | 3 | 0.434... s | 0.379... s | 0.349... s 
| 5 | 0.742... s | 0.650... s | 0.618... s | 5 | 0.411... s | 0.364... s | 0.336... s 
| 3 | 0.406... s | 0.358... s | 0.328... s | 4 | 1.662... s | 1.456... s | 1.334... s 
| 4 | 0.776... s | 0.662... s | 0.620... s | 3 | 0.258... s | 0.227... s | 0.213... s  

Right now time complexity of the program is too high, but the fastest way to copy the rack seems to be iterating the rack and making shallow copies of the sublists. 

### Possible improvements
I could add a game that can be played with two players instead of playing against an ai. I could also make a pygame implementation of the program.

### Sources
- "Tiralabra - 2023 loppukesä", viewed 24 August 2023, https://tiralabra.github.io/2023_loppukesa/index
- "Connect Four", Wikipedia, wiki article, viewed 22 July 2023, https://en.wikipedia.org/wiki/Connect_Four
- "Minimax" 2023, Wikipedia, wiki article, viewed 22 July 2023, https://en.wikipedia.org/wiki/Minimax
- "Alpha-beta-pruning" 2023, Wikipedia, wiki article, viewed 22 July 2023, https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
- "Minimax-pelit", viewed 22 July 2023, https://tiralabra.github.io/2023_loppukesa/fi/aiheet/minimax.pdf
- Kuo, J. 2020, "Artificial Intelligence at Play — Connect Four (Mini-max algorithm explained)", Analytics Vidhya, Medium, viewed 17 August 2023, https://medium.com/analytics-vidhya/artificial-intelligence-at-play-connect-four-minimax-algorithm-explained-3b5fc32e4a4f (for heuristic scoring)
- "unittest.mock — mock object library", viewed 24 August 2023, https://docs.python.org/3/library/unittest.mock.html
- "math — Mathematical functions", viewed 30 August 2023, https://docs.python.org/3/library/math.html
- "copy — Shallow and deep copy operations", viewed 28 August 2023, https://docs.python.org/3/library/copy.html
- "Python | Ways to print list without quotes", GeeksforGeeks, viewed 29 August 2023, https://www.geeksforgeeks.org/python-ways-to-print-list-without-quotes/
