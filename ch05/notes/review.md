In this chapter, we looked at three ways to parametrize tests:

* We can parametrize test functions, creating many test cases, when we apply the `@pytest.mark.parametrize()` decorator.
* We can parametrize fixtures with `@pytest.fixture(params=())`. This is helpful if the fixture needs to do different work based on the parameter values.
* We can generate complex parametrization sets with `pytest_generate_tests`.

We also looked at how we can run subsets of parametrized test cases using `pytest -k`.

While the techniques for parametrization covered in this chapter are quite powerful, when you start using parametrization in your own testing, you may run into more complex parameter set needs, such as needing to

* parametrize multiple parameters with all three techniques,
* combine techniques,
* use lists and generators for parametrization,
* create custom identifiers (which is especially useful when parametrizing with object values), or
* use indirect parametrization.

We’ll cover these advanced scenarios in "Advanced Parametrization", in the third course in this series, "pytest Booster Rockets".