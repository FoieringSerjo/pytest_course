## Review 

* We installed the cards application with 
```
(course) $pip install ./cards_proj
```

* pytest uses assert rewriting, which allows us to use standard Python assert
expressions.

* Tests can fail from assertion failures, from calls to`pytest.fail()`, or from any
uncaught exception.
* `pytest.raises()` is used to test for expected exceptions.
* Structure tests with Given-When-Then or Arrange-Act-
Assert.
* Classes can be used to group tests.
* Running small subsets of tests is handy while debugging, and pytest
allows you to run a small batch of tests in many ways.

### Flags used so far
* `-v` verbose output
* `-vv`  shows even more information during test failures.
* `--tb=no` turns off tracebacks
* `-k` to select tests on keyword expressions
* `--no-summary` to turn off summary output.