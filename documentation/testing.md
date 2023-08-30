# Testing document
### Unit testing
Right now, unit testing covers classes gamestatus, gamerack, score and minimax well. Class gameloop is not covered well, since I have some trouble testing while loops and raising errors.

### Coverage report
<img width="683" alt="Screenshot 2023-08-30 at 20 15 07" src="https://github.com/lottapispa/connect-four-tiralabra/assets/101987621/abb06835-d48d-44c8-9f12-d12589c65dd6">

### Performance evaluation


### How to re-test
This command shows you the tests: `poetry run invoke test` and this command gets you the test coverage report: `poetry run invoke coverage-report`. You can open the report from the command line.
