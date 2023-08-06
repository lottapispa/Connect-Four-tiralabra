# Testing document
### Unit testing
<img width="694" alt="Screenshot 2023-08-06 at 19 07 23" src="https://github.com/lottapispa/connect-four-tiralabra/assets/101987621/b2599944-3060-4f06-b5ff-0d05574c3441">

This command gets you the test coverage report: `poetry run invoke coverage-report`. Right now, unit testing mostly covers class gamestatus. It doesn't cover class minimax as it's not functional yet. Class gameloop is also not covered well, since I had some trouble testing inputs.

### How to re-test
This command shows you the tests: `poetry run invoke test`. 
