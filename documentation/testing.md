# Testing document
### Unit testing
Right now, unit testing covers classes gamestatus, gamerack, score and minimax well. Class gameloop is not covered well, since I have some trouble testing while loops.

### Coverage report
<img width="679" alt="Screenshot 2023-08-31 at 23 17 04" src="https://github.com/lottapispa/connect-four-tiralabra/assets/101987621/4d360392-e91a-4a43-8cfb-6ef833503001">

### Performance evaluation
The time it takes to call choose_best_move in main loop with different ways to make a copy of the rack.
| **move** | **deepcopy** | **json** | **copy sublists in for loop** | **move** | **deepcopy** | **json** | **copy sublists in for loop**
| --------- | ----------- | -------- | ---------------------------- | -------- | ------------ | -------- | -------------------- 
| 4 | 0.486... s | 0.423... s | 0.384... s | 4 | 0.483... s | 0.427... s | 0.392... s
| 3 | 0.833... s | 0.739... s | 0.645... s | 5 | 0.739... s | 0.648... s | 0.596... s 
| 2 | 0.943... s | 0.828... s | 0.756... s | 3 | 0.434... s | 0.379... s | 0.349... s 
| 5 | 0.742... s | 0.650... s | 0.618... s | 5 | 0.411... s | 0.364... s | 0.336... s 
| 3 | 0.406... s | 0.358... s | 0.328... s | 4 | 1.662... s | 1.456... s | 1.334... s 
| 4 | 0.776... s | 0.662... s | 0.620... s | 3 | 0.258... s | 0.227... s | 0.213... s  

The fastest way to copy the rack seems to be iterating the rack and making copies of the sublists and appending them to one list. 

### How to re-test
This command shows you the tests: `poetry run invoke test` and this command gets you the test coverage report: `poetry run invoke coverage-report`. You can open the report from the command line.
