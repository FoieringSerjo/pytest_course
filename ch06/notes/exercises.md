Using markers for test selection is a powerful pytest capability to help run a subset of tests. Walking through these exercises will help you get comfortable
with them.

The directory `exercises/ch06` has a couple of files:

```
exercises/ch06
├── pytest.ini
└── test_markers.py
```

`test_markers.py` includes seven test cases:

```
$ cd ch6/exercises
$ pytest -v
========================= test session starts ==========================
collected 7 items
test_markers.py::test_one PASSED [ 14%]
test_markers.py::test_two PASSED [ 28%]
test_markers.py::test_three PASSED [ 42%]
test_markers.py::TestClass::test_four PASSED [ 57%]
test_markers.py::TestClass::test_five PASSED [ 71%]
test_markers.py::test_param[6] PASSED [ 85%]
test_markers.py::test_param[7] PASSED [100%]
```

1. Modify `pytest.ini` to register three markers, `odd`, `testclass`, and `all`.
2. Mark all the odd test cases with `odd`.
3. Use a file level marker to add the `all` marker.
4. Mark the test class with the `testclass` marker.
5. Run all the tests using the `all` marker.
6. Run the `odd` tests.
7. Run the `odd` tests that are not marked with `testclass`.
8. Run the `odd` tests that are parametrized. (Hint: Use both marker and keyword flags.)