# Testing document
### Unit testing
Right now, unit testing covers classes gamestatus, gamerack and score. It doesn't cover class minimax as it's not functional yet. Class gameloop is also not covered well, since I have some trouble testing while loops and raising errors.

### Coverage report
<img width="686" alt="Screenshot 2023-08-27 at 19 07 44" src="https://github.com/lottapispa/connect-four-tiralabra/assets/101987621/9ad00b1a-cb5e-42ac-af62-085064d78539">

### Performance evaluation


### How to re-test
This command shows you the tests: `poetry run invoke test` and this command gets you the test coverage report: `poetry run invoke coverage-report`. You can open the report from the command line.
