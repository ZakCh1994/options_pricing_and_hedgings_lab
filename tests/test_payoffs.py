import numpy as np

from options_lab.payoffs import(
    call_payoff,
    put_payoff,
    long_forward_payoff,
    short_forward_payoff,
    short_call_payoff,
    short_put_payoff,
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

    np.testing.assert_array_equal(long_payoff, -short_payoff)

def test_long_and_short_call_options_payoffs_are_opposites():
    spots = np.array([80, 100, 120])
    delivery_price = 100

    long_call = call_payoff(spots, delivery_price) 
    short_call = short_call_payoff(spots, delivery_price)

    np.testing.assert_array_equal(long_call, -short_call)

def test_long_and_short_put_options_payoffs_are_opposites():
    spots = np.array([80, 100, 120])
    delivery_price = 100

    long_put = put_payoff(spots, delivery_price) 
    short_put = short_put_payoff(spots, delivery_price)

    np.testing.assert_array_equal(long_put, -short_put)
