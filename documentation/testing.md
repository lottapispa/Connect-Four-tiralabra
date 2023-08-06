# Testing document
### Unit testing
This command gets you the test coverage report: `poetry run invoke coverage-report`. Right now, unit testing mostly covers class gamestatus, except for an unfinished function. It doesn't cover class minimax as it's not functional yet. Class gameloop is also not covered well, since I had some trouble testing inputs.

### How to re-test
This command shows you the tests: `poetry run invoke test`. 
