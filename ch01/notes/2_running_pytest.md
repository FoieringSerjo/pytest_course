## Running pytest

* `pytest`
  * search this dir and sub-dirs for tests
* `pytest <filename> [<filename>] ...`
  * run these specific test files
* `pytest <dirname> [<dirname>] ...`
    * run these specific test dirs
* `pytest <file|dir> [<file|dir>] ...`
  * you can mix and match
* `pytest -v` or `pytest --verbose`
    * shows function and "PASSED" | "FAILED" instead of dots and Fs.
* `pytest --tb=no`
    * hide the traceback
