When people start working with parametrization, I’ve noticed that many tend to favor the technique they learned first—usually function parametrization — and seldom use the other methods.

Working through these exercises will help you learn how easy all three techniques are. Then later, in your own testing, you’ll be able to chose from three tools and select which is most useful to you at the time.

We’ve tested `finish()` already. But there’s another similar API method that needs testing, `start()`:


```
# cards_proj/src/cards/api.py

def start(self, card_id: int):
"""Set a card state to 'in prog'."""
   self.update_card(card_id, Card(state="in prog"))
```

Let’s build some parametrized tests for it:
1. Write out three test functions that make sure any start state results in
"in prog" when `start()` is called:
   * `test_start_from_done()`
   * `test_start_from_in_prog()`
   * `test_start_from_todo()`
2. Write a `test_start()` function that uses function parametrization to test the three test cases.
3. Rewrite `test_start()` using fixture parametrization.
4. Rewrite `test_start()` using `pytest_generate_tests`.

For Exercise 3 and Exercise 4, you can re-use the `start_state` fixture and the `pytest_generate_tests` implementation if you put the `test_start()` function in the same file as `test_finish()`.

Shared fixtures, even parametrized ones, and `pytest_generate_tests` can also be placed in `conftest.py` and shared between many test files. However, in our case,
if we try to put a `start_state` fixture in `conftest.py` and a `pytest_generate_tests` hook function that parametrizes `start_state`, it won’t work. pytest will notice the collision and give us a duplicate `start_state` error. This, of course, is not a problem normally, as we don’t usually use two methods for parametrizing the same
parameter.