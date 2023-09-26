# Testing document
### Unit testing
Right now, unit testing covers classes gamestatus, gamerack and score well. Class gameloop could be covered better, but is good enough. Even though class minimax is technically covered it could use better and more thorough testing. User inputs have been tested well, the program is prepared for wrong inputs including TypeErrors and asks the user for input again if it was wrong. 

### Coverage report
<img width="688" alt="Screenshot 2023-09-26 at 13 20 40" src="https://github.com/lottapispa/connect-four-tiralabra/assets/101987621/c74a2146-24cf-45c0-b648-0c917bcbaa8d">

### How to re-test
This command shows you the tests: `poetry run invoke test` and this command gets you the test coverage report: `poetry run invoke coverage-report`. You can open the report from the command line.
