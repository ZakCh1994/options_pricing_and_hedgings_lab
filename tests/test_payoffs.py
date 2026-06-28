import numpy as np

from options_lab.payoffs import(
    call_payoff,
    put_payoff,
    long_forward_payoff,
    short_forward_payoff
)

def test_call_payoff_for_array_input()