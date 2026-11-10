# Quant training handoff

Last updated: 10 November 2026.

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

## Dice exercise: core work and Monte Carlo extension completed

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
- The trading conclusion now compares expected profits and correctly chooses doing nothing. Zak revised his example to dice (3, 4); discussed that receiving EUR 4 after paying EUR 4.60 gives a loss of EUR 0.60. The original paragraph's long-run wording is informal; the discussion distinguished negative expectation from guaranteed finite-sample loss.
- No reusable discrete-model module or corresponding automated tests have been created in this session. Existing payoff code was not changed.
- Python fluency is still developing: Zak requested reminders about array creation, `np.arange`, `np.maximum` and broadcasting, and benefited from breaking the Boolean-counting task into smaller steps. Continue with manageable tasks and leave the first implementation to him.

### Progress on 10 November: checks, functions and simulation

- Zak accumulated the six enumerated probabilities with `+=`; saved total is 1.0. Initially indexed a scalar probability as `prob[k]`, causing an IndexError; corrected this by counting the probability for the current k inside the loop.
- Added correct assertions using `np.isclose` for total probability and the independently derived expectation. Discussed that assertions continue silently when true and raise AssertionError when false, and that normalisation alone does not establish the whole distribution.
- Wrote `dice_maxima(n_faces)` in the notebook for positive integer inputs, returning the enumerated maxima table. Added correct hand-written checks with `np.array_equal` for one-faced and two-faced dice. Source reviewed; the function cell still has a null execution count, so its saved state does not establish that those assertions ran. No separate module or automated test file was created.
- Generated reproducible samples using `np.random.default_rng(42)` and `rng.integers(1, 7, size=(n, 2))`. Initially produced shape (2, 1000), then corrected to one dice pair per row. Used `np.max(rolls, axis=1)` and averaged the resulting payouts. Discussed axes, slicing, shape, print labels and f-strings; briefly explained uniform floats and categorical draws.
- Distinguished exhaustive enumeration and floating-point rounding from Monte Carlo sampling error. Removed a simulation assertion using default `np.isclose` against the exact expectation; it required an inappropriate level of agreement for random sampling.
- Implemented estimated standard error as sample standard deviation divided by sqrt(n), using `ddof=1`. Explained the N-1 denominator and unbiased sample variance, including that the square-root standard deviation estimate is not itself exactly unbiased.
- Saved 1,000-trial output reviewed earlier: mean 4.453, exact-minus-estimated discrepancy about 0.01922, estimated SE about 0.04499. Current saved 4,000-trial output: mean 4.43675, discrepancy about 0.03547, estimated SE about 0.02243 and standardised estimated-minus-exact discrepancy about -1.5812.
- Correctly predicted that quadrupling trials halves standard error. Needed clarification that a realised discrepancy can increase on a particular run while estimator precision improves.
- Constructed approximate 95% confidence intervals using mean +/- 1.96 * estimated SE. Discussed the CLT, why one SE corresponds to about 68% normal coverage and 1.96 SE to about 95%, and that coverage concerns the fixed expectation rather than individual payouts or the sample mean inside its own interval.
- Replaced an assertion requiring interval coverage with an observational if/else check: valid intervals can miss the truth. Implemented repeated experiments, initialising the generator outside the loop. Initially used `for i in 3`; corrected to `range(3)`.
- Correctly counted coverage across 200 experiments of 4,000 dice pairs. Saved output is 97%, i.e. 194 intervals cover the true expectation and six miss. Discussed random variation around nominal coverage and the distinction between more trials per experiment and more experiments.
- Zak wrote a coverage interpretation. Following feedback, the assistant corrected its final saved wording at Zak's documentation request: separate estimates per experiment, narrower intervals do not guarantee coverage, and sample means become less dispersed too. Understanding has been discussed but should be reinforced naturally in later applications.
- Final application discussed algebraically: at an ask of EUR 4.45, shift an expected-payout interval [L,U] to [L-4.45,U-4.45] for expected buyer profit. Width and SE are unchanged. The reviewed single-run interval includes zero after this shift, although the exact expected profit is about EUR 0.02222. Zak recognised the need for greater precision to assess its sign from simulation.
- Added a final notebook Markdown reminder at Zak's request: more trials reduce sampling uncertainty without removing the risk of individual-contract losses; confidence intervals rely on the assumed model. No code for the profit-interval application was assigned or implemented.
- Verification: inspected notebook source and saved outputs, not a fresh full notebook execution. No pytest run on 10 November. Repeated-experiment code reuses names such as `simulated_mean` and `lower_bound`, overwriting the earlier single-run variables; rerun the appropriate cell before using its results. No commits or pushes requested or performed.

## Next steps

1. If switching machines, pull the same branch and check the local project/environment as needed.
2. Begin a new practice lesson on one-period binomial pricing through replication. This direction was proposed and recorded at Zak's request; no numerical problem has yet been assigned and no solution has been revealed.
3. Start with the structure and assumptions: one asset, two possible terminal prices, a European option and a cash account with a stated growth factor; frictionless trading, borrowing/lending and short selling as needed, no dividends, and both states possible. Choose numbers satisfying the no-arbitrage condition. Ask Zak to calculate the option's two terminal payoffs first, then guide him to match them with asset and cash holdings. Leave the derivation and first implementation to him.
4. Use replication to motivate the no-arbitrage price before introducing risk-neutral probabilities. Explicitly distinguish this from expected-profit calculations under the dice model and from pricing by real-world expected payoff. Keep the first step small; no need to create code files or restructure the project in advance. Existing reusable payoff functions can support the lesson when implementation is warranted.
5. Refine the remaining training schedule towards pricing, risk and data after assessing his starting level. The earlier weekly plan was provisional; no detailed revised schedule has been agreed.

## Switching computers

Before leaving a machine, ask Codex to update this handoff, then review, commit and push the relevant files. On the other machine, clone the repository once or pull the same branch, open it in VS Code, and start a conversation with:

> Read AGENTS.md and TRAINING_PROGRESS.md. Resume our quant training from the recorded next step, using hints and leaving the first implementation to me.

Pushing this repository transfers tracked files, including this handoff; it does not transfer the original local chat transcript.
