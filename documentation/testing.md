# Testing document
### Unit testing
Right now, unit testing mostly covers classes gamestatus and gamerack. It doesn't cover class minimax as it's not functional yet. Class score has one function whose test doesn't work yet, but most of the functions are covered. Class gameloop is also not covered well, since I had some trouble testing for wrong inputs.

### Coverage report
<img width="681" alt="Screenshot 2023-08-26 at 23 02 07" src="https://github.com/lottapispa/connect-four-tiralabra/assets/101987621/6f11ae97-3166-4da1-86ea-e32c1bc70527">

### Performance evaluation


### How to re-test
This command shows you the tests: `poetry run invoke test` and this command gets you the test coverage report: `poetry run invoke coverage-report`. You can open the report from the command line.
