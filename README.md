# Options Pricing and Hedging Lab

A learning portfolio of derivative pricing, simulation and risk analysis in Python. The notebooks record reasoning, implementation, checks and ongoing practice for quantitative finance roles. Synthetic interview exercises are practice cases, not claims about an employer's actual assessment.

## Projects

| Project | Notebook | Focus |
| --- | --- | --- |
| 1 | [Payoffs and profit](notebooks/01_payoffs_intro.ipynb) | Vectorised call, put and forward payoffs and plots |
| 2 | [Discrete models and Monte Carlo](notebooks/02_discrete_models.ipynb) | Exact enumeration, simulation and sampling uncertainty |
| 3 | [Binomial replication](notebooks/03_binomial_replication.ipynb) | Replication, backward induction and European call/put pricing; in progress |
| 4 | [Option portfolio under a spot shock](notebooks/04_option_portfolio_spot_shock.ipynb) | CSV preparation, duplicate handling, pandas merges and delta-based scenario P&L; in progress |

Project 4 uses the synthetic [positions](data/04_option_portfolio_spot_shock/positions.csv) and [market](data/04_option_portfolio_spot_shock/market.csv) tables. Its notebook records outstanding coverage reporting and interpretation tasks. It is a learning draft, not a completed risk report.

Reusable calculations live in `src/options_lab/`; automated checks live in `tests/`. See [TRAINING_PROGRESS.md](TRAINING_PROGRESS.md) for demonstrated progress and open learning tasks.

## Set up and run

Python 3.13 is the currently verified interpreter. Create a local virtual environment rather than transferring one between computers:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Open a notebook in VS Code with the Python and Jupyter extensions, select this repository's `.venv` as its kernel, and run all cells from a fresh kernel. Notebook paths support starting in the repository root or `notebooks/` directory. Project 4's data is included; no absolute personal file paths are required.

Run the automated tests from the repository root:

```powershell
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m pytest
```

## Further learning

Consolidate the binomial pricing engine and its input validation, complete the spot-shock case, then explore fixed-maturity trees, convergence, American exercise, Black–Scholes pricing and hedging. These are proposed extensions, not implemented features.
