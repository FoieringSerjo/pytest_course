# Review

## Virtual Environments

* Create
  * `$ python3 -m venv venv --prompt course`
* Activate
  * `$ source venv/bin/activate`
  * `C:\> venv\Scripts\activate.bat`
  * `PS C:\> venv\Scripts\Activate.ps1`
* Deactivate
  * `$ deactivate`
   
## Installing pytest

```
(course) $ pip install pytest
```

## Running pytest

* `pytest`
* `pytest <file|dir> [<file|dir>] ...`
* `pytest -v` or `pytest --verbose`
* `pytest --tb=no`

------

## Test Discovery

* Test files should be named `test_<something>.py` or `<something>_test.py`.
* Test methods and functions should be named `test_<something>`.
* Test classes should be named `Test<Something>`.

---

## Test Outcomes

Possible outcomes of a test function
* PASSED (.) 
* FAILED (F) - exception in test
* SKIPPED (s) - marked to skip 
* XFAIL (x) - marked as expected to fail
* XPASS (X) - expected to fail but passed
* ERROR (E) - exception in fixture
