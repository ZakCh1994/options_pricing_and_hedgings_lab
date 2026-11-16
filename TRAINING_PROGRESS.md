# Quant training progress

Last updated: 16 November 2026.

## Current focus and next step

**Current position:** Project 3 is in progress. One-period call/put replication, risk-neutral valuation and put–call parity have been covered with guidance. The two-period call example includes self-financing rebalancing and terminal-payoff checks. Zak is now generalising backward induction to multiple periods.

**Next concrete step:** revisit the last cell of `notebooks/03_binomial_replication.ipynb`. Zak has created terminal `call_payoffs` and changed the loop bound to depend on input length. His `backward_step` still accepts stock prices and applies `call_payoff` inside. Help him revise it to accept option values and perform one weighted, discounted backward step. The reason for applying the payoff function only at expiry was just explained and needs confirmation through his attempt. Leave the implementation to Zak. Then reuse the function on its output until one initial value remains, comparing the two-period result with the existing replication example.

Read `AGENTS.md` for lasting teaching preferences. This file records project progress and handoff context; it is not a full conversation transcript. Verify relevant project state before relying on historical notes.

## Training direction

Prepare for institutional Quant Analyst work and relevant Quant Developer skills, with Van Lanschot Kempen QED-type roles as a benchmark. Develop Python fluency alongside mathematical reasoning, pricing, risk and data skills. Use hints, manageable steps and the cycle: formulate -> predict -> implement -> test -> explain.

The earlier weekly plan was provisional; no detailed revised schedule has been agreed. Do not use the old Excel preparation tracker.

## Project 1: Payoffs and profit

**Status:** existing payoff implementation and introductory notebook available; reuse these foundations in later pricing work. The original implementation dates and full teaching history are not recorded here.

**Aim:** express long/short call, put and forward payoffs, distinguish payoff from profit, and develop vectorised Python calculations with independent checks.

**Files:**

- `src/options_lab/payoffs.py`
- `tests/test_payoffs.py`
- `notebooks/01_payoffs_intro.ipynb`

**Recorded outcome:** the module implements vectorised long/short call, put and forward payoffs. Seven tests cover independently known values and long/short sign relationships. The notebook contains payoff plotting code and saved outputs. Cash-flow understanding was reinforced in Project 2; do not infer complete mastery of pricing from the existence of payoff code.

### Dated progress

- **7 November 2026:** the handoff records seven passing pytest tests on the desktop using the existing `.venv` and `PYTHONPATH=src`. The introductory notebook was inspected but not freshly executed.
- **10 November 2026:** module and test source inspected again while reorganising this handoff. No changes to those files and no fresh test execution.

## Project 2: Discrete models and Monte Carlo

**Status:** core exercise and simulation extension completed with guidance. Continue reinforcing interpretation in later applications; completion does not imply independent fluency in every concept.

**Aim:** connect a derived probability distribution to exact enumeration, expected trading profits, simulation estimates and uncertainty.

**File:** `notebooks/02_discrete_models.ipynb`. The exploratory function and assertions remain in this notebook. No `src/options_lab/discrete_models.py` or `tests/test_discrete_models.py` exists as of the 10 November file inspection.

### Problem and established results

Two independent fair six-sided dice are rolled. The contract pays `X = max(D1, D2)` euros. Settlement is immediate, with no transaction costs; the objective is expected profit without a risk penalty. The dealer bid is EUR 4.20 and ask EUR 4.60. The choices are buy one, sell one or do nothing.

- Zak derived `P(X <= k) = k^2/36`, `P(X = k) = (2k - 1)/36` for integer `k = 1, ..., 6`, and `E[X] = 161/36` euros.
- Buying gives `X - ask`; selling gives `bid - X`. Expected buyer profit is approximately EUR -0.1278 and seller profit EUR -0.2722, so doing nothing maximises expected profit.
- Positive payout does not imply positive profit. Positive expected profit does not guarantee profit on an individual contract. These are expectations under the stated dice model, not a general derivative-pricing rule or an arbitrage argument.

### Demonstrated work and points to reinforce

- Built all 36 ordered outcomes with NumPy arrays, reshaping and broadcasting; counted probabilities and checked the expected payout against independently derived mathematics.
- Wrote `dice_maxima(n_faces)` for positive integer inputs and hand-written one-face/two-face checks. Used `assert`, `np.isclose` for floating-point results and `np.array_equal` for integer arrays.
- Generated reproducible dice pairs, calculated row maxima and estimated their mean. Implemented sample standard deviation, standard error, approximate 95% confidence intervals and repeated-experiment coverage.
- Correctly predicted that quadrupling trials halves standard error. Discussed why realised error can nevertheless increase on a particular run.
- Needed repeated explanation of sample standard deviation versus standard error, actual discrepancy versus estimated uncertainty, and confidence-interval coverage. Reinforce these through applications rather than assuming they are fully consolidated.
- Corrected confusion between the fixed true expectation and each interval's sample mean, and between trials per experiment and number of experiments. Every constructed interval contains its own centre; coverage asks whether it contains the true expectation.
- Python still benefits from short steps: scalar versus array indexing, shapes and axes, `range`, accumulation, indentation, retaining results, seed placement and displaying output. Leave the first implementation to Zak.

### Dated progress

**7 November 2026 — exercise recorded**

The dice problem and the cumulative-probability hint were recorded as unattempted. No solution had been supplied at that handoff.

**9 November 2026 — derivation and exact enumeration**

- Derived the distribution and expectation. Initially used a single-die variable when differencing cumulative probabilities, and reversed the seller's profit sign; corrected both after feedback.
- Created the notebook with the problem, derivation, `(6, 6)` maxima table, probability loop and buyer/seller profit arrays. Reviewed source and saved outputs agreeing with the theoretical results.
- Understood that buying at an ask of EUR 4.40 has positive expected profit but can lose on a roll of (1, 1). Discussed long-run average profit without claiming guaranteed loss over every finite sequence.

**10 November 2026 — checks and reusable function**

- Added probability accumulation and assertions for total probability and expected payout. Corrected an attempt to index a scalar as `prob[k]`.
- Implemented `dice_maxima(n_faces)` and assertions against `[[1]]` and `[[1, 2], [2, 2]]`. Source was correct on review; the function cell's null execution count does not verify that the assertions ran.

**10 November 2026 — simulation and uncertainty**

- Used `np.random.default_rng(42)`, `rng.integers(1, 7, size=(n, 2))` and `np.max(rolls, axis=1)`. Corrected the initial `(2, 1000)` orientation. Practised slicing, output labels and f-strings; briefly discussed sampling floats and letters.
- Replaced a strict simulation-versus-exact assertion with an assessment of sampling uncertainty. Implemented `estimated_se = np.std(simulated_maxima, ddof=1) / np.sqrt(simulated_maxima.size)`.
- Explained the N-1 sample-variance denominator, including that unbiased variance does not imply exactly unbiased sample standard deviation.
- Reviewed these saved results for seed 42:

| Trials per experiment | Estimated mean (EUR) | Exact minus estimated (EUR) | Estimated SE (EUR) |
| --- | --- | --- | --- |
| 1,000 | 4.453 | 0.01922 | 0.04499 |
| 4,000 | 4.43675 | 0.03547 | 0.02243 |

The 1,000-trial result was inspected earlier; the notebook was subsequently changed to 4,000 trials. The latter estimate was about 1.58 standard errors below the truth.

- Constructed `mean +/- 1.96 * estimated_se`. Explained the normal approximation, approximately 68% coverage for one SE and 95% for 1.96 SE, and why coverage is not a guarantee. Removed an assertion requiring every interval to contain the benchmark.
- Wrote a loop with the generator initialised outside it, correcting `for i in 3` to `range(3)`. Counted **194 covering intervals out of 200 experiments**, each with 4,000 dice pairs: **97% observed coverage**. Discussed sampling variation around nominal 95% coverage.
- Zak wrote a conclusion. At his documentation request, the assistant clarified its coverage wording and corrected the missing “not” in “does not guarantee”.

**10 November 2026 — application to expected profit and closure**

- Discussed shifting `[L,U]` to `[L-a,U-a]` for expected buyer profit at fixed ask `a`; standard error and width stay unchanged.
- At an ask of EUR 4.45, the reviewed single-run profit interval includes zero although exact expected profit is approximately EUR 0.02222. Zak recognised that greater simulation precision would help assess the sign. This application was discussed algebraically; no new implementation was assigned.
- Added the final Markdown reminder: more trials reduce sampling uncertainty without removing individual-contract loss risk; intervals depend on the assumed model. Closed this learning block and selected binomial replication as the next direction.

### Verification and notebook cautions

Source and saved outputs were reviewed; the assistant did not freshly execute the whole notebook or run pytest during this project session. A null execution count is not proof of a successful run. Notebook changes were sometimes unsaved, so save before requesting review.

The repeated-experiment cell overwrites names such as `simulated_mean` and `lower_bound` from the earlier single-run cell. Rerun the relevant cell before reusing its results. The initial trading conclusion retains informal long-run wording; the discussion distinguished negative expectation from certain finite-sample loss.

## Project 3: Binomial pricing, replication and backward induction

**Status:** in progress. The one-period and explicit two-period examples have been worked through with guidance. General multi-period implementation remains unfinished.

**Aim:** connect statewise replication, no-arbitrage pricing, risk-neutral valuation and dynamic hedging, then implement backward induction for a recombining tree.

**Files:** `notebooks/03_binomial_replication.ipynb`, reusing `src/options_lab/payoffs.py`. Pricing functions and exploratory checks currently live in the notebook.

### Established work, recorded 13 November 2026

These notes summarise the intervening training discussions and notebook reviews. Individual earlier session dates were not recorded here.

- Used a practice model with stock price EUR 100, terminal prices EUR 120/80, strike EUR 100 and cash growth factor `R=1.05`. Assumptions include no dividends, frictionless trading, fractional shares, short selling and borrowing/lending at the same rate. Both states are possible.
- Derived call replication with delta `0.5`, cash `-800/21` euros and initial price `250/21`, approximately EUR 11.904762. Negative cash denotes borrowing. Worked through arbitrage cash flows for both an underpriced and an overpriced call.
- Distinguished stock price, strike, option premium, terminal payoff and financing cost. Matching both state payoffs determines the replication cost independently of real-world state probabilities.
- Derived risk-neutral up weight `q=(R*S_0-S_d)/(S_u-S_d)=5/8` and the discounted weighted-payoff price. Zak showed algebraically that this equals the replicating portfolio cost. Discussed real-world expected payoff EUR 16 with up probability 80%, and the strict no-arbitrage condition `S_d < R*S_0 < S_u`, including stock/cash arbitrage when it fails.
- Wrote one-period call and put pricing functions and a general `replicate_one_period` function. Its tuple contains delta, cash, q, replication price and risk-neutral price, in that order. Assertions check both state payoffs and agreement of pricing methods.
- Explored call strike EUR 110 and a strike above both terminal prices. Derived put delta `-0.5`, cash `60/1.05` euros and price approximately EUR 7.142857. Checked put–call parity `C_0-P_0=S_0-K/R` with `np.isclose`, discussing floating-point rounding.
- Resolved notebook imports using the existing source-path setup. Practised retaining full function results, tuple indexing and execution order. A running kernel previously masked a variable used before assignment, which was subsequently reordered.

### Two-period replication and hedging, reviewed 13 November 2026

- Extended the model with `u=1.2`, `d=0.8` and `R=1.05` per period, European expiry at `t=2`. Terminal stock prices are EUR 64, 96 and 144, with call payoffs EUR 0, 0 and 44.
- Worked backwards from final payoffs to continuing option values at `t=1`. Up-node value is approximately EUR 26.190476 and down-node value is zero. Reinforced why immediate exercise value EUR 20 at the up node is different from the continuing European option value.
- Calculated initial price approximately EUR 15.589569 and checked against `44*q**2/R**2`. Initial delta is approximately 0.654762 and cash approximately EUR -49.886621. After an up move, delta is `11/12` and cash approximately EUR -83.809524. After a down move, both holdings are zero.
- Verified self-financing rebalancing in both states with assertions. Buying approximately 0.261905 extra shares after an up move requires additional borrowing. After a down move, selling the initial shares raises approximately EUR 52.380952, exactly repaying the accrued loan.
- Checked up–down and up–up terminal portfolio values against call payoffs, using the rebalanced cash position. Saved execution count 20 showed no errors and price output EUR 15.590. Zero holdings after the first down move explain zero terminal payoffs along both remaining paths.

### Current multi-period attempt and open learning point, 13 November 2026

- Generated the `n+1` terminal stock prices in ascending order using a list comprehension with `S_0*u**k*d**(n-k)`. Correctly paired neighbouring children in a discounted risk-neutral calculation.
- For `n=3`, reviewed saved output `[0, 9.04761905, 48.76190476]` for the three option values at `t=2`. Discussed shrinking layers `4 -> 3 -> 2 -> 1` and constant `q=(R-d)/(u-d)` when multipliers and the cash growth factor are the same at every node.
- Introduced NumPy slices `[:-1]` and `[1:]` for neighbouring pairs. Zak currently uses a list comprehension, which can remain while he consolidates the calculation.
- Latest saved cell uses `n=2`, creates `stock_prices` and a separate `call_payoffs` array, and bounds the function's loop with `len(stock_prices)-1`. The function still applies `call_payoff` internally and is still called with stock prices. Revision to operate directly on option values is pending.
- Explained why applying the payoff function to a continuing option value would lose that value. Terminal payoffs are calculated once, then every backward step weights and discounts the resulting child option values. Zak asked for this explanation immediately before ending the session, so understanding remains to be checked through his implementation.
- Latest cell has a null execution count with retained output `[0, 26.19047619]` and terminal payoffs `[0, 0, 44]`. Treat that output as retained evidence, not fresh verification of the current source. No complete multi-period pricer has been implemented or verified.

### Session resumed, 16 November 2026

- Confirmed that the 13 November handoff was saved and includes the one-period theory, two-period replication, self-financing checks and unfinished multi-period function.
- Reinspected the last notebook cell after Zak reported a computer shutdown. The saved implementation remains at the pending revision described above. No new completed calculation or demonstrated understanding has been recorded since that handoff.
- Restated the immediate task: make `backward_step` accept child option values, use the input length for neighbouring pairs, and apply it first to `call_payoffs` and then to its own result. With the current `n=2`, array lengths should shrink `3 -> 2 -> 1`, with the final value checked against the earlier two-period replication price.
- Supplied terminal commands to stage the notebook and handoff, commit and push to `origin main`. Completion of those user-run commands has not been verified.

### Verification and continuation

The assistant reviewed notebook source and saved outputs, without freshly executing the notebook or pytest during this block. Save and rerun relevant cells when resuming, checking kernel state if behaviour differs. Continue with the pending `backward_step` revision before adding a loop over all periods. Keep the project open and preserve Zak's first implementation.

## Environment, verification and repository history

- **7 November 2026:** seven tests passed on the desktop using `.venv` and `PYTHONPATH=src`. The initial sandbox launch failed; the authorised run outside the sandbox succeeded. No fresh tests were run on 9 or 10 November.
- **7 November 2026:** Git was available; branch `main` tracked `origin/main`, with no divergence from the locally stored remote reference. No fresh remote fetch was performed. This is historical state, not a current sync check.
- `AGENTS.md` was tracked in commit `53d3cb9` (`Add quant training instructions`); Zak reported pushing it successfully.
- **10 November 2026:** provided terminal commands for Zak to commit and push the notebook and handoff. Completion of that user-run push has not been verified. The assistant has not committed or pushed these updates.
- The laptop's repository and Python environment have not been verified. Virtual environments are machine-specific; verify or recreate the environment rather than copying the desktop `.venv`.

## Keeping this handoff current

Keep each project's aim, status, files, demonstrated progress and open learning points concise. Add dated notes inside the relevant project for meaningful session progress. Update the current focus at the top when changing projects. Distinguish source inspection, saved outputs, fresh execution and user reports; preserve unanswered exercises without solutions.

When switching computers, update this handoff, review the changes, then commit and push when requested. On the other machine, clone once or pull the same branch and check the local environment as needed. Resume with:

> Read AGENTS.md and TRAINING_PROGRESS.md. Resume our quant training from the recorded next step, using hints and leaving the first implementation to me.

The repository transfers tracked files, including this handoff; it does not transfer the original local chat transcript.
