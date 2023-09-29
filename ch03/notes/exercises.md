Fixtures are often one of the trickier parts of pytest for people to get used to.

Going through the following exercises will

* help solidify your understanding of how fixtures work,
* allow you to use different fixture scopes, and
* internalize the run sequence with the visual output of `--setup-show`.
 
1. Create a test file called `test_fixtures.py`.
2. Write a few data fixtures—functions with the `@pytest.fixture()` decorator that return some data (perhaps a list, dictionary, or tuple).
3. For each fixture, write at least one test function that uses it.
4. Write two tests that use the same fixture.
5. Run `pytest --setup-show test_fixtures.py`. Are all the fixtures run before every test?
6. Add `scope='module'` to the fixture from Exercise 4.
7. Re-run `pytest --setup-show test_fixtures.py`. What changed?
8. For the fixture from Exercise 6, change `return <data>` to `yield <data>`.
9. Add print statements before and after the yield.
10. Run `pytest -s -v test_fixtures.py`. Does the output make sense?
11. Run `pytest --fixtures`. Can you see your fixtures listed?
12. Add a docstring to one of your fixtures, if you didn't include them already.
    Re-run `pytest --fixtures` to see the description show up.