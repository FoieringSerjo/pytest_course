In this chapter, we looked at the `tmp_path`, `tmp_path_factory`, `capsys`, and `monkeypatch` builtin fixtures:
 
* The `tmp_path` and `tmp_path_factory` fixtures are used to for temporary directories. `tmp_path` is function scope, and `tmp_path_factory` is session scope. Related fixtures not covered in the chapter are `tmpdir` and `tmpdir_factory`.
* `capsys` can be used to capture `stdout` and `stderr`. It can also be used to temporarily turn off output capture. Related fixtures are `capsysbinary`, `capfd`, `capfdbinary`, and `caplog`.
* `monkeypatch` can be used to change the application code or the environment. We used it with the Cards application to redirect the database location to a temporary directory created with `tmp_path`.
* You can read about these and other fixtures with `pytest --fixtures` or in the API docs at https://docs.pytest.org/en/latest/reference/reference.html