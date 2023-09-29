## Exercises


 
1. The file `test_card_mod.py` in `exercises/ch02` is a copy of `test_card.py`, but the import statement is replaced with the definition of the Card class.
Modify default values in the Card definition. For example, replace some
None values with an empty string or a filled-in string. Do the tests catch the changes?
2. What happens if we change `compare=False` to `compare=True`?
3. Are there any missing tests? Any functionality not covered? Add some
test functions if there is something missing.
4. Try the `-k` option to select a test.

Using the options as they come up in the course will help you to get used to the flexibility of the pytest command line. Even if you don’t remember the options, if you use them a couple of times, you’ll remember that the functionality is there, and can look for it again in `pytest --help` if you ever need it in the future.
