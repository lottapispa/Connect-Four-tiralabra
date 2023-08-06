# Testing document
### Unit testing
<img width="686" alt="Screenshot 2023-08-06 at 17 55 05" src="https://github.com/lottapispa/connect-four-tiralabra/assets/101987621/37740c28-2bc6-4c12-acae-ed6db29fad8a">
This command gets you the test coverage report: `poetry run invoke coverage-report`. Right now, unit testing mostly covers class gamestatus, except for an unfinished function. It doesn't cover class minimax as it's not functional yet. Class gameloop is also not covered well, since I had some trouble testing inputs.

### How to re-test
This command shows you the tests: `poetry run invoke test`. 
