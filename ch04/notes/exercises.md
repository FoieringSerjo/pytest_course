Reaching for builtin fixtures whenever possible is a great way to simplify your own test code. The exercises below are designed to give you experience using `tmp_path` and `monkeypatch`, two super handy and common builtin fixtures.

Take a look at this script that writes to a file:


```python
# ch04/hello_world.py

def hello():
    with open("hello.txt", "w") as f:
        f.write("Hello World!\n")

if __name__ == "__main__":
    hello()
```
1. Write a test without fixtures that validates that `hello()` writes the correct content to `hello.txt`.
2. Write a second test using `tmp_path` that utilizes a temporary directory and `monkeypatch.chdir()`.
3. Add a print statement to see where the temporary directory is located. Manually check the `hello.txt` file after a test run. 