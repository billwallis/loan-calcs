<div align="center">

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![tests](https://github.com/billwallis/loan-calcs/actions/workflows/tests.yaml/badge.svg)](https://github.com/billwallis/loan-calcs/actions/workflows/tests.yaml)
[![coverage](coverage.svg)](https://github.com/dbrgn/coverage-badge)
[![GitHub last commit](https://img.shields.io/github/last-commit/billwallis/loan-calcs)](https://shields.io/badges/git-hub-last-commit)

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/billwallis/loan-calcs/main.svg)](https://results.pre-commit.ci/latest/github/billwallis/loan-calcs/main)

</div>

---

# Loan Calculations

Library for common loan calculations.

## Notation

A _loan_ is a fixed value of money borrowed by an entity and usually repaid over a series of instalments.

The following notation is used throughout this project for loans:

- `L`: Loan amount
- `R`: Periodic interest rate
- `N`: Total number of repayments
- `P_n`: Total periodic repayment value at period `n`
- `P_{P, n}`: The principal part of the periodic repayment value at period `n`
- `P_{I, n}`: The interest part of the periodic repayment value at period `n`
- `b`: Whether the interest is applied before or after the repayment
- `B_n`: The balance on the loan at period `n`

The repayment for a loan, `P_n`, is split into two parts:

- The _principal_ part, `P_{P, n}`, which is paying off the original money that was borrowed.
- The _interest_ part, `P_{I, n}`, which is paying off the interest applied on the loan.

In 'real life', a loan can have other components such as fees. These are outside the scope of this project.

## Calculations

Many of the properties are calculated analytically. The calculations are described in the [`tex/proofs.pdf`](tex/proofs.pdf) file.
