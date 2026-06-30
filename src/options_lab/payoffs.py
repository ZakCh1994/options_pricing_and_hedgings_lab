import numpy as np

def call_payoff(spot_at_maturity, strike):
    spot_at_maturity = np.asarray(spot_at_maturity, dtype=float)
    return np.maximum(spot_at_maturity - strike, 0)

def put_payoff(spot_at_maturity, strike):
    spot_at_maturity = np.asarray(spot_at_maturity, dtype=float)
    return np.maximum(strike - spot_at_maturity, 0)

def short_call_payoff(spot_at_maturity, strike):
    return -call_payoff(spot_at_maturity, strike)

def short_put_payoff(spot_at_maturity, strike):
    return -put_payoff(spot_at_maturity, strike)

def long_forward_payoff(spot_at_maturity, delivery_price):
    spot_at_maturity = np.asarray(spot_at_maturity, dtype=float)
    return spot_at_maturity - delivery_price

def short_forward_payoff(spot_at_maturity, delivery_price):
    spot_at_maturity = np.asarray(spot_at_maturity, dtype=float)
    return delivery_price - spot_at_maturity

