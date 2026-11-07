# Quant training handoff

Last updated: 7 November 2026.

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
- All seven existing pytest tests passed on the desktop on 7 November 2026 using the existing `.venv` and `PYTHONPATH=src`. The initial sandbox launch failed; the authorised run outside the sandbox succeeded.
- `notebooks/01_payoffs_intro.ipynb` was inspected and contains payoff plotting code and stored outputs. It has not been freshly executed during this conversation.
- Git is now available on the desktop. At handoff creation, the current branch was `main`, tracking `origin/main`, with no divergence reported against the locally stored remote reference. No fresh remote fetch was performed.
- `AGENTS.md` is tracked in commit `53d3cb9` (`Add quant training instructions`). Zak reported pushing it successfully.
- The laptop's repository, branch, Python environment and tests have not been checked. Virtual environments are machine-specific; verify or set up the laptop environment rather than copying the desktop `.venv`.

## Current exercise: not yet attempted

Two independent fair six-sided dice are rolled. A contract pays, in euros,

    X = max(D1, D2).

Assume immediate settlement, no transaction costs, and an objective of maximising expected profit without a risk penalty.

- Dealer bid: EUR 4.20. Selling one contract receives EUR 4.20 and creates an obligation to pay X.
- Dealer ask: EUR 4.60. Buying one contract costs EUR 4.60 and receives X.
- Available actions: buy one, sell one or do nothing.

Tasks: derive the distribution of X, calculate its expected payoff, select the action with greatest expected profit, and explain whether positive expected profit guarantees a profit.

The only mathematical hint supplied so far is:

    P(X <= k) = P(D1 <= k, D2 <= k), for k = 1, ..., 6.

The pending question is: what does independence let you do with the right-hand side, and what is P(Di <= k)?

Zak has not yet supplied an attempt. No complete distribution, expectation, trading decision or implementation has been revealed. Resume with his reasoning rather than a solution.

## Next steps

1. If switching machines, pull the same branch and check the local project/environment as needed.
2. Invite Zak's answer to the pending probability question and critically review it.
3. Guide the derivation before asking him to implement reusable calculations and meaningful tests himself.
4. Possible future files are `src/options_lab/discrete_models.py`, `tests/test_discrete_models.py` and `notebooks/02_discrete_models.ipynb`; they have not been created as part of this training conversation.
5. Refine the remaining training schedule towards pricing, risk and data after assessing his starting level. The earlier weekly plan was provisional; no detailed revised schedule has been agreed.

## Switching computers

Before leaving a machine, ask Codex to update this handoff, then review, commit and push the relevant files. On the other machine, clone the repository once or pull the same branch, open it in VS Code, and start a conversation with:

> Read AGENTS.md and TRAINING_PROGRESS.md. Resume our quant training from the recorded next step, using hints and leaving the first implementation to me.

Pushing this repository transfers tracked files, including this handoff; it does not transfer the original local chat transcript.
