# Testing document
### Unit testing
Right now, unit testing mostly covers classes gamestatus and gamerack. It doesn't cover class minimax as it's not functional yet. Class gameloop is also not covered well, since I had some trouble testing inputs. Class score has some unfinished functions that don't have tests yet, but the working functions are covered.

### Coverage report
<img width="681" alt="Screenshot 2023-08-20 at 20 06 08" src="https://github.com/lottapispa/connect-four-tiralabra/assets/101987621/a7cc42b7-a762-487a-8246-338116b2cdc6">

### Performance evaluation


### How to re-test
This command shows you the tests: `poetry run invoke test` and this command gets you the test coverage report: `poetry run invoke coverage-report`. You can open the report from the command line.
