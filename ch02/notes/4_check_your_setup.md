## Check your setup
Make sure you have everything installed correctly.  
If this doesn't work, please stop and fix before moving on. 
 
* Navigate to the ch02 directory. 
* Run `pytest test_card.py`.

You should see something like this:
```
``$ pytest test_card.py
========================= test session starts ==========================
collected 7 items
test_card.py ....... [100%]
========================== 7 passed in 0.07s ===========================
```

If you are not able to run pytest, or don’t get seven passing tests, something’s wrong.  

Please try to resolve these issues before attempting to go further.

These are things that might have gone wrong:
* You installed pytest in a virtual environment, but forgot to activate the environment.
* You have pytest and cards installed in separate environments.
* `pip list --not-required` shows all top level packages you have installed. Make sure both pytest and cards show up in the list.

Still having issues? reach out.
 
* File an issue at `https://github.com/okken/pytest_primary_power`
* More ways to get help to come.
 
