# Quant training progress

Last updated: 10 November 2026.

## Current focus and next step

**Current position:** the dice exercise and its Monte Carlo extension are complete for this learning stage. The next learning block is **one-period binomial pricing through replication**.

**Next concrete step:** introduce a small two-state asset model and a European option, then ask Zak to calculate the two terminal option payoffs. No numerical problem has been assigned yet. Guide the replication argument afterwards, leaving the derivation and first implementation to him.

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

## Project 3: One-period binomial pricing and replication

**Status:** planned; not started. Recorded as the next direction on **10 November 2026**. No numerical exercise, solution or implementation has been assigned.

**Aim:** derive a European option's no-arbitrage price by matching its terminal payoffs with asset and cash holdings, then connect replication to risk-neutral probabilities.

**Planned teaching sequence:**

1. Introduce one asset with two possible terminal prices, a European option and a cash account with a stated growth factor. State timing, units, no dividends, frictionless trading and permitted borrowing/lending and short selling. Both states are possible; choose numbers satisfying the no-arbitrage condition.
2. Ask Zak to calculate the option's two terminal payoffs. This is the next concrete task; keep it small.
3. Guide him to match both payoffs with asset and cash holdings and interpret their initial cost. Leave the algebra and first implementation to him.
4. Introduce risk-neutral probabilities after replication. Distinguish no-arbitrage pricing from real-world expected-payoff and expected-profit calculations.

Reuse existing payoff functions when useful. No new notebook or module has been created for this block; create files when the lesson warrants them.

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
