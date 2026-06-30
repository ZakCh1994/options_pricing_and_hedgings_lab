# Options Pricing and Hedging Lab   

A python project containing general derivative pricing ideas.

Current features:

- long/short call payoff features
- long/short put payoff features
- long/short forward payoff features
- unit tests with pytest
- basic payoff visualisation in Jupyter notebooks

## Runing the tests

'''powershell  
$env:PYTHONPATH = "src"  
pytest

## Roadmap

- Add profit diagrams including option premiums
- Implement forward pricing under deterministic interest rates
- Implement one-step and multi-step binomial trees
- Price European and American options
- Implement Black-Scholes formulas
- Add Greeks
- Simulate delta hedging under geometric Brownian motion