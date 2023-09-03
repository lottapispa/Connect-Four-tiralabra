# Testing document
### Unit testing
Right now, unit testing covers classes gamestatus, gamerack, score and minimax well. Class gameloop is not covered well enough, since I have some trouble testing while loops. User inputs have been tested well, the program is prepared for wrong inputs including TypeErrors and asks the user for input again if it was wrong.

### Coverage report
<img width="678" alt="Screenshot 2023-09-02 at 23 48 16" src="https://github.com/lottapispa/connect-four-tiralabra/assets/101987621/5f234488-aa4c-4858-b014-0df6f70d2e1f">

### How to re-test
This command shows you the tests: `poetry run invoke test` and this command gets you the test coverage report: `poetry run invoke coverage-report`. You can open the report from the command line.
