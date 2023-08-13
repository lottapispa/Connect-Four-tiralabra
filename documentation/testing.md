# Testing document
### Unit testing
This command gets you the test coverage report: `poetry run invoke coverage-report`. Right now, unit testing mostly covers classes gamestatus and gamerack. It doesn't cover class minimax as it's not functional yet. Class gameloop is also not covered well, since I had some trouble testing inputs.

### Coverage report
<img width="681" alt="Screenshot 2023-08-09 at 19 15 01" src="https://github.com/lottapispa/connect-four-tiralabra/assets/101987621/1bc5dc4a-9766-4931-ba24-ad161a6bb7e7">

### Performance evaluation


### How to re-test
This command shows you the tests: `poetry run invoke test`. 
