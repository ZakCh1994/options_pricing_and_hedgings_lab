"""Bond pricing and zero-curve interpolation for cash-flow schedules."""

import numpy as np
import pandas as pd


def bond_prices_calculator(coupons, zero_rates, payment_years_sorted, shock_basis=0):
    """Price one bond from aligned Series of cash flows, percentage rates and years.

    The optional shock is in basis points and can be a scalar or a Series with
    the same index as the rates. Rates are continuously compounded.
    """
    adjusted_rates = (zero_rates + shock_basis / 100) / 100
    return sum(
        coupons.iloc[i] * np.exp(-adjusted_rates.iloc[i] * payment_years_sorted.iloc[i])
        for i in range(len(payment_years_sorted))
    )


def linear_inter(lower_time, lower_value, upper_time, upper_value, middle_time):
    """Interpolate a value at a time between two distinct quoted maturities."""
    width = upper_time - lower_time
    return (
        np.abs(middle_time - lower_time) / width * upper_value
        + np.abs(upper_time - middle_time) / width * lower_value
    )


def bond_prices(cashflows, curve):
    """Return base and shocked prices in euros per bond.

    Cash-flow columns are bond_id, payment_years and cashflow_eur. Curve columns
    are maturity_years, zero_rate_pct and shock_bps. Maturities must be unique
    and span the payment dates. Output columns are bond_id, price and shock_price.
    """
    schedules = cashflows[["bond_id", "payment_years", "cashflow_eur"]]
    quotes = curve[["maturity_years", "zero_rate_pct", "shock_bps"]]
    matched = schedules.merge(
        quotes.rename(columns={"maturity_years": "payment_years"}),
        how="left",
        on="payment_years",
        validate="many_to_one",
    )

    missing_years = matched.loc[matched["zero_rate_pct"].isna(), "payment_years"].drop_duplicates()
    quotes_by_year = quotes.set_index("maturity_years")
    maturities = quotes_by_year.index
    outside_curve = (missing_years < maturities.min()) | (missing_years > maturities.max())
    if outside_curve.any():
        raise ValueError("Payment years fall outside the quoted curve range.")

    # Build a lookup once for the payment dates shared across bonds.
    interpolated_rows = []
    for year in missing_years:
        lower_year = maturities[maturities < year].max()
        upper_year = maturities[maturities > year].min()
        lower = quotes_by_year.loc[lower_year]
        upper = quotes_by_year.loc[upper_year]
        interpolated_rows.append({
            "payment_years": year,
            "interpolated_rate_pct": linear_inter(
                lower_year, lower["zero_rate_pct"], upper_year, upper["zero_rate_pct"], year
            ),
            "interpolated_shock_bps": linear_inter(
                lower_year, lower["shock_bps"], upper_year, upper["shock_bps"], year
            ),
        })

    interpolated = pd.DataFrame(
        interpolated_rows,
        columns=["payment_years", "interpolated_rate_pct", "interpolated_shock_bps"],
    )
    matched = matched.merge(interpolated, how="left", on="payment_years")
    matched["zero_rate_pct"] = matched["zero_rate_pct"].fillna(matched["interpolated_rate_pct"])
    matched["shock_bps"] = matched["shock_bps"].fillna(matched["interpolated_shock_bps"])

    rows = []
    for bond_id, schedule in matched.groupby("bond_id"):
        amounts = schedule["cashflow_eur"]
        rates = schedule["zero_rate_pct"]
        years = schedule["payment_years"]
        rows.append({
            "bond_id": bond_id,
            "price": bond_prices_calculator(amounts, rates, years),
            "shock_price": bond_prices_calculator(amounts, rates, years, schedule["shock_bps"]),
        })

    return pd.DataFrame(rows, columns=["bond_id", "price", "shock_price"])
