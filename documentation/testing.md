# Testing document
### Unit testing
Right now, unit testing covers classes gamestatus, gamerack and score. It doesn't cover class minimax yet. Class gameloop is also not covered well, since I have some trouble testing while loops and raising errors.

### Coverage report
<img width="685" alt="Screenshot 2023-08-27 at 22 56 16" src="https://github.com/lottapispa/connect-four-tiralabra/assets/101987621/49a3e02f-2b93-4456-88fc-d825d8e0a160">

### Performance evaluation


### How to re-test
This command shows you the tests: `poetry run invoke test` and this command gets you the test coverage report: `poetry run invoke coverage-report`. You can open the report from the command line.
