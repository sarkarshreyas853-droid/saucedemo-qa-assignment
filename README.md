# SauceDemo QA Automation

Selenium (Python) tests for https://www.saucedemo.com, written with pytest.

## Tests included

1. `tests/test_login.py`: valid login with `standard_user` reaches the inventory page.
2. `tests/test_locked_user.py`: login with `locked_out_user` shows the "locked out" error message.
3. `tests/test_checkout.py`: login, add an item to the cart, complete checkout, and check the "Thank you for your order!" confirmation.

## Requirements

- Python 3.12
- Microsoft Edge
- Install packages: `pip install selenium pytest`

## How to run

Run all tests:

    pytest

Run one test:

    pytest tests/test_login.py

The tests open Edge, run the steps, and close it. Running all three takes about 3 minutes.

## Notes

- All users use the password `secret_sauce`.
- The bug report and test plan are in this repository.# SauceDemo QA Automation

Selenium (Python) tests for https://www.saucedemo.com, written with pytest.

## Tests included

1. `tests/test_login.py`: valid login with `standard_user` reaches the inventory page.
2. `tests/test_locked_user.py`: login with `locked_out_user` shows the "locked out" error message.
3. `tests/test_checkout.py`: login, add an item to the cart, complete checkout, and check the "Thank you for your order!" confirmation.

## Requirements

- Python 3.12
- Microsoft Edge
- Install packages: `pip install selenium pytest`

## How to run

Run all tests:

    pytest

Run one test:

    pytest tests/test_login.py

The tests open Edge, run the steps, and close it. Running all three takes about 3 minutes.

## Notes

- All users use the password `secret_sauce`.
- The bug report and test plan are in this repository.