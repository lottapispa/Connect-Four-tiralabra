# Testing document
### Unit testing
Right now, unit testing covers classes gamestatus, gamerack, score and minimax well. Class gameloop could be covered better, but is good enough. User inputs have been tested well, the program is prepared for wrong inputs including TypeErrors and asks the user for input again if it was wrong.

### Coverage report
<img width="684" alt="Screenshot 2023-09-03 at 21 50 54" src="https://github.com/lottapispa/connect-four-tiralabra/assets/101987621/e5e54b0c-1748-48d2-af09-0058717b83e0">

### How to re-test
This command shows you the tests: `poetry run invoke test` and this command gets you the test coverage report: `poetry run invoke coverage-report`. You can open the report from the command line.
