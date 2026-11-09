# Quant training handoff

Last updated: 9 November 2026.

## How to resume

Read `AGENTS.md` for teaching preferences. This file records progress rather than the complete conversation. Continue from the next step below; do not assume that proposed work is complete.

## Aim and working method

- Prepare for institutional Quant Analyst roles and relevant quantitative finance interviews, with Van Lanschot Kempen QED-type work as a benchmark.
- Develop Python fluency alongside mathematical reasoning, pricing, risk and data skills.
- Use reusable modules, exploratory notebooks and separate tests in the existing repository.
- Give hints before solutions and let Zak write the first exercise implementation.
- Do not use the old Excel preparation tracker.

## Confirmed project state

- Existing modules implement vectorised long/short call, put and forward payoffs in `src/options_lab/payoffs.py`.
- Historical verification: all seven existing pytest tests passed on the desktop on 7 November 2026 using the existing `.venv` and `PYTHONPATH=src`. The initial sandbox launch failed; the authorised run outside the sandbox succeeded. Tests were not rerun during the 9 November training session.
- `notebooks/01_payoffs_intro.ipynb` was inspected and contains payoff plotting code and stored outputs. It has not been freshly executed during this conversation.
- Historical Git check on 7 November: the current branch was `main`, tracking `origin/main`, with no divergence reported against the locally stored remote reference. Git was available on the desktop. No fresh remote fetch was performed; Git state was not rechecked on 9 November.
- `AGENTS.md` is tracked in commit `53d3cb9` (`Add quant training instructions`). Zak reported pushing it successfully.
- The laptop's repository, branch, Python environment and tests have not been checked. Virtual environments are machine-specific; verify or set up the laptop environment rather than copying the desktop `.venv`.

## Dice exercise: calculations verified; conclusion wording needs refinement

Two independent fair six-sided dice are rolled. A contract pays, in euros,

    X = max(D1, D2).

Assume immediate settlement, no transaction costs, and an objective of maximising expected profit without a risk penalty.

- Dealer bid: EUR 4.20. Selling one contract receives EUR 4.20 and creates an obligation to pay X.
- Dealer ask: EUR 4.60. Buying one contract costs EUR 4.60 and receives X.
- Available actions: buy one, sell one or do nothing.

Tasks: derive the distribution of X, calculate its expected payoff, select the action with greatest expected profit, and explain whether positive expected profit guarantees a profit.

### Demonstrated mathematical and financial progress

- Zak correctly used independence and fairness to derive `P(X <= k) = k^2/36` for integer `k = 1, ..., 6`.
- Initially wrote the difference of cumulative probabilities for a single die rather than X. After feedback, correctly derived `P(X = k) = (2k - 1)/36` and `E[X] = 161/36` euros.
- Initially reversed the seller's profit sign and needed the contract cash flows explained. After discussion, understood that buying gives `X - ask`, selling gives `bid - X`, and doing nothing gives exactly zero profit.
- At the original quotes, expected buyer profit is approximately EUR -0.1278 and expected seller profit is approximately EUR -0.2722. Zak correctly concluded that doing nothing maximises expected profit under the stated objective.
- Understood that negative expected profit can coexist with profitable individual outcomes. Discussed convergence of average profit under independent repetition, rather than guaranteed loss over every finite sequence.
- Correctly explained that buying at an ask of EUR 4.40 gives positive expected profit without guaranteeing profit: a roll of (1, 1) produces a loss. This is an expectation calculation under the stated dice model, not a general derivative-pricing rule or an arbitrage argument.

### Python work reviewed on 9 November

- Zak created `notebooks/02_discrete_models.ipynb`, containing the problem and mathematical derivation, including the support `k = 1, ..., 6`.
- With syntax hints, used `np.arange(1, 7)`, reshaping to `(6, 1)` and `(1, 6)`, and broadcasting with `np.maximum` to enumerate the maxima of all 36 equally likely ordered dice pairs.
- Used Boolean comparisons and `np.count_nonzero` to calculate a probability, then wrote a loop over all six values. Saved probability outputs match the derived distribution.
- Used `np.mean(maxima)` to check the expectation; the saved difference from `161/36` is zero. This is exhaustive enumeration, not Monte Carlo simulation; decimal results are subject to floating-point rounding.
- Correctly implemented `seller_profit = 4.20 - maxima`, `buyer_profit = maxima - 4.60`, and the mean of each array.
- After Zak saved again, the code and stored outputs were inspected: execution count 19, with printed seller and buyer means of approximately -0.2722 and -0.1278, consistent with the source. These are saved execution results; the assistant did not freshly execute the notebook. The means are printed together without labels, which is correct but could be clearer.
- The final Markdown conclusion is now present and correctly chooses doing nothing. It says "maximises the profit" and compares "payoff" values; the remaining refinement is to say "maximises expected profit" and consistently compare expected profits. Ask Zak to add why a positive payout can still lead to a loss (purchase cost). Leave this small revision to him.
- No reusable discrete-model module or corresponding automated tests have been created in this session. Existing payoff code was not changed.
- Python fluency is still developing: Zak requested reminders about array creation, `np.arange`, `np.maximum` and broadcasting, and benefited from breaking the Boolean-counting task into smaller steps. Continue with manageable tasks and leave the first implementation to him.

## Next steps

1. If switching machines, pull the same branch and check the local project/environment as needed.
2. Ask Zak to refine the conclusion in `notebooks/02_discrete_models.ipynb`: doing nothing maximises expected profit, and the comparison is between expected profits rather than payoffs. Add a sentence explaining why a positive payout can still produce a loss. The saved code and both mean-profit outputs have now been reviewed and are correct.
3. Once the notebook is finalised, introduce meaningful numerical checks one at a time, starting with probabilities summing to one. Let Zak write the check; explain floating-point comparison tolerances when needed. Then consider turning the enumeration into a small reusable function, with an independently known boundary case, before moving to simulation and sampling uncertainty.
4. Possible future files are `src/options_lab/discrete_models.py` and `tests/test_discrete_models.py`; neither has been created in this session. Keep exploratory work in the existing notebook until a reusable function is warranted. No new unanswered mathematical exercise has been assigned.
5. Refine the remaining training schedule towards pricing, risk and data after assessing his starting level. The earlier weekly plan was provisional; no detailed revised schedule has been agreed.

## Switching computers

Before leaving a machine, ask Codex to update this handoff, then review, commit and push the relevant files. On the other machine, clone the repository once or pull the same branch, open it in VS Code, and start a conversation with:

> Read AGENTS.md and TRAINING_PROGRESS.md. Resume our quant training from the recorded next step, using hints and leaving the first implementation to me.

Pushing this repository transfers tracked files, including this handoff; it does not transfer the original local chat transcript.
