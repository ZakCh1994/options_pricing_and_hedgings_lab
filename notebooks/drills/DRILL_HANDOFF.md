# Python drill handoff

Read the [training progress](../../TRAINING_PROGRESS.md) for the broader interview and project history and follow the [repository instructions](../../AGENTS.md) for tutoring. Use this handoff for the current drill sequence and [01_drill.ipynb](01_drill.ipynb) for starter data and saved answers. Git ignores the local drill notebooks.

## Goal

Build enough Python fluency for Zak to turn an idea into working code during the Van Lanschot Kempen case interview. Practise data handling with pandas and numerical calculations with NumPy. Zak reports feeling more comfortable reasoning through a case than recalling the exact syntax. The recruiter recommended brushing up on Python and reading the case brochure thoroughly once it arrives. Use that brochure to guide practice when Zak shares it.

Zak chose short chat-guided tasks that he types and runs in his notebook. Give one plain-English prompt in chat and put any starter data in a notebook code cell. Leave space for an unaided first attempt. When he says **check**, inspect the saved cell and its output. Confirm correct work or give one focused hint. If the saved output looks stale, verify against the saved code in a fresh process. A small intermediate result often helps him see where the code and his mental model diverge. Track whether he recalls the pattern unaided, needs a syntax hint, or needs to inspect the object before proceeding.

## Where to resume

**Next drill.** Start Drill 7 with a short NumPy task on fresh data. Ask Zak to work across all scenarios at once using the full array. Use the attempt to check how he aligns a vector with a two-dimensional array and chooses the axis to sum over.

### Completed drills

- **Drill 1, position limits.** After hints, Zak combined two Boolean masks, allowed the boundary values and returned the breached trade IDs in input order as a Python list.
- **Drill 2, net units by desk.** After hints, Zak grouped signed positions, kept the desk with a zero total and produced a DataFrame with `desk` and `net_units` as columns.
- **Drill 3, daily P&L by book.** Independently looped over the pandas groups, counted trades with `len(group)` and summed P&L. The saved output retained the zero-total book. Adjusted the dictionary key order after feedback to match the requested column order.
- **Drill 4, present value by scenario.** Independently calculated both prices by slicing and reducing one scenario column at a time. After a hint, put the two scalars into a NumPy array. A fresh run confirmed shape `(2,)` and values EUR 113.56 and EUR 110.08 in base and shocked order.
- **Drill 5, match positions to spot quotes.** Independently used a left merge on the underlying with `validate="many_to_one"`. The saved output kept all five positions in input order, quoted both trades in the repeated underlying and retained the missing quote.
- **Drill 6, remaining order quantities.** Completed with hints on tuple unpacking, dictionary assignment, tracking the running quantity and copying the input. The first working loop modified the starter dictionary, so rerunning subtracted every fill again. The final cell produced the correct quantities twice in the same fresh Python session and preserved the starter dictionary. Revisit unpacking and updating a dictionary keyed by ID on a later task.

## What to strengthen

1. **Know what each pandas expression returns.** Practise distinguishing a Series, a DataFrame, a `GroupBy` object and an aggregated result. Group by a column name such as `desk`, then inspect an individual group if needed. Check whether the group labels are in the index or a column before selecting, renaming or reshaping.
2. **Keep row-level checks separate from whole-table checks.** A comparison between a Series and a scalar gives one Boolean per row. Writing `[mask]` creates a one-item list containing the mask. Practise combining masks with `|` or `&`, using `.any()` when one matching row is enough and `all()` when every check must pass. Drill 1 also showed the need to select the ID Series before converting it to a list. The bond case showed that asserting a nonempty set of Booleans can pass even when it contains `False`.
3. **Trace how values line up.** Revisit label-based `.loc`, positional `.iloc` and Series alignment during assignment and arithmetic. In the bond case, a Series indexed by the three bond-price rows left six of nine cash-flow rows unfilled. Practise merging by an ID and reading values inside `.assign()` from the DataFrame that pandas passes to the lambda.
4. **Refresh core Python syntax in small doses.** Revisit what the loop variable receives when iterating over a list of dictionaries, unpacking two values from `zip()`, and using a dictionary keyed by ID. Include default arguments, adding a scalar to a Series and placing the `for` clause inside `sum(...)`. Zak has seen all of these patterns in the bond case. Recall on new tasks is still worth checking.

Zak made progress when he printed a single `GroupBy` group and recognised it as the same rows his earlier Boolean mask selected. He used that pattern to price one bond at a time. He also traced the interpolation weights at an endpoint and implemented a guard for out-of-range dates. Build on that way of reasoning by asking him to predict or inspect one intermediate result at a time.

## NumPy and numerical practice

Alternate numerical drills with pandas and core Python so all three get regular practice.

- **Array shapes and axes.** Predict the output shape before running an expression. Practise elementwise operations, broadcasting and summing along the intended axis in a small payment-by-scenario array.
- **Pricing and risk calculations.** Use small examples involving discount factors, interpolation or scenario P&L. State the units and predict the sign and rough magnitude before calculating. The bond case provides a starting point for practising conversions between basis points, percentage points and decimal rates, and preserving the signs of position quantities.
- **Independent checks.** Compare one entry with a hand calculation or known benchmark. For floating-point results, practise choosing a suitable tolerance with `np.isclose` or `np.allclose`. Pair a zero-shock check with a nonzero benchmark. Zero stays zero under either unit conversion, so the nonzero example checks the scale.

Once these patterns are familiar, an occasional short mini-case can combine pandas input preparation, a NumPy calculation and a brief explanation of the result. Add simple labelled plots when they help explain the output.

## Start a new chat

> Read `AGENTS.md`, `TRAINING_PROGRESS.md` and `notebooks/drills/DRILL_HANDOFF.md`. Resume from the next drill. Give me one prompt in chat to attempt unaided, put any starter data in `notebooks/drills/01_drill.ipynb` and check my saved notebook when I say check.
