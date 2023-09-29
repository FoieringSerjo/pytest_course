In this chapter, we covered a lot about fixtures:

* Fixtures are `@pytest.fixture()` decorated functions.
* Test functions or other fixtures depend on a fixture by putting its name in their parameter list.
* Fixtures can return data using return or yield.
* Code before the yield is the setup code. Code after the yield is the teardown code.
* Fixtures can be set to function, class, module, package, or session scope.
  The default is function scope. You can even define the scope dynamically.
 
* Multiple test functions can use the same fixture.
* Multiple test modules can use the same fixture if it’s in a `conftest.py` file.
* Multiple fixtures at different scope can speed up test suites while maintaining test isolation.
 
* Tests and fixtures can use multiple fixtures.
* `autouse` fixtures don’t have to be named by the test function.
* You can have the name of a fixture be different from the fixture function name.

We also covered a few new command-line flags:

* `pytest --setup-show` is used to see the order of execution.
* `pytest --fixtures` is used to list available fixtures and where the fixture is located.
* `pytest --fixtures-per-test`
* `-s` and `--capture=no` allow print statements to be seen even in passing tests.