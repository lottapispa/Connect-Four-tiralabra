# Testing document
### Unit testing
Right now, unit testing mostly covers classes gamestatus and gamerack. It doesn't cover class minimax as it's not functional yet. Class score has some unfinished functions that don't have tests yet, but the working functions are covered. Class gameloop is also not covered well, since I had some trouble testing for wrong inputs.

### Coverage report
<img width="683" alt="Screenshot 2023-08-20 at 23 45 25" src="https://github.com/lottapispa/connect-four-tiralabra/assets/101987621/30e17085-f33a-4ae3-ac09-eb7933950718">

### Performance evaluation


### How to re-test
This command shows you the tests: `poetry run invoke test` and this command gets you the test coverage report: `poetry run invoke coverage-report`. You can open the report from the command line.
