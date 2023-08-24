# Testing document
### Unit testing
Right now, unit testing mostly covers classes gamestatus and gamerack. It doesn't cover class minimax as it's not functional yet. Class score has one function whose test doesn't work yet, but most of the functions are covered. Class gameloop is also not covered well, since I had some trouble testing for wrong inputs.

### Coverage report
<img width="679" alt="Screenshot 2023-08-24 at 23 56 03" src="https://github.com/lottapispa/connect-four-tiralabra/assets/101987621/c285f16b-7d57-47b6-8479-6116fcf92c0c">

### Performance evaluation


### How to re-test
This command shows you the tests: `poetry run invoke test` and this command gets you the test coverage report: `poetry run invoke coverage-report`. You can open the report from the command line.
