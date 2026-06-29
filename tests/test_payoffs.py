import numpy as np

from options_lab.payoffs import(
    call_payoff,
    put_payoff,
    long_forward_payoff,
    short_forward_payoff
)

def test_call_payoff_for_array_input():
    spots = np.array([80, 100, 120])
    strike = 100

    result = call_payoff(spots, strike)

    expected = np.array([0, 0, 20])

    np.testing.assert_array_equal(result, expected)

def test_put_payoff_for_array_input():
    spots = np.array([80, 100, 120])
    strike = 100

    result = put_payoff(spots, strike)

    expected = np.array([20, 0, 0])

    np.testing.assert_array_equal(result, expected)

def test_long_forward_payoff_for_array_input():
    spots = np.array([80, 100, 120])
    delivery_price = 100

    result = long_forward_payoff(spots, delivery_price)

    expected = np.array([-20, 0, 20])

    np.testing.assert_array_equal(result, expected)

def test_short_forward_payoff_for_array_input():
    spots = np.array([80, 100, 120])
    delivery_price = 100

    result = short_forward_payoff(spots, delivery_price)

    expected = np.array([20, 0, -20])

    np.testing.assert_array_equal(result, expected)

def test_long_and_short_forward_payoffs_are_opposites():
    spots = np.array([80, 100, 120])
    delivery_price = 100

    long_payoff = long_forward_payoff(spots, delivery_price) 
    short_payoff = short_forward_payoff(spots, delivery_price)

    expected = np.array([0, 0, 0])

    np.testing.assert_array_equal(long_payoff, -short_payoff)

