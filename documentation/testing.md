# Testing document
### Unit testing
Right now, unit testing mostly covers classes gamestatus and gamerack. It doesn't cover class minimax as it's not functional yet. Class gameloop is also not covered well, since I had some trouble testing inputs. Class score is still empty right now.

### Coverage report
<img width="682" alt="Screenshot 2023-08-13 at 23 45 02" src="https://github.com/lottapispa/connect-four-tiralabra/assets/101987621/eb0ce857-a878-43aa-816d-78104c515ad0">

### Performance evaluation


### How to re-test
This command shows you the tests: `poetry run invoke test` and this command gets you the test coverage report: `poetry run invoke coverage-report`. You can open the report from the command line.
