"""
Unit tests for the ``src.main`` module.
"""

import decimal

import loan_calcs


def test__fixed_principal_loan(
    fixed_principal_loan: loan_calcs.FixedPrincipalLoan,
):
    """
    Test that a fixed principal loan is generated correctly.
    """

    repayment = decimal.Decimal("166.6666666666666666666666667")
    assert fixed_principal_loan.principal_repayment == repayment
    assert fixed_principal_loan.periodic_repayment == repayment

    def bal(period: int) -> decimal.Decimal:
        return fixed_principal_loan.calculate_balance_at_period(period)

    assert bal(period=0) == decimal.Decimal(1000)
    assert bal(period=1) == decimal.Decimal("833.3333333333333333333333333")
    assert bal(period=2) == decimal.Decimal("666.6666666666666666666666666")
    assert bal(period=3) == decimal.Decimal("499.9999999999999999999999999")
    assert bal(period=4) == decimal.Decimal("333.3333333333333333333333332")
    assert bal(period=5) == decimal.Decimal("166.6666666666666666666666665")
    assert bal(period=6) == decimal.Decimal(0)


def test__fixed_repayment_loan(
    fixed_repayment_loan: loan_calcs.FixedRepaymentLoan,
):
    """
    Test that a fixed repayment loan is generated correctly.
    """

    assert fixed_repayment_loan.total_repayments == 15

    def bal(period: int) -> decimal.Decimal:
        return fixed_repayment_loan.calculate_balance_at_period(period)

    # TODO: This feels wrong, shouldn't a fixed repayment decrease the same amount each month?
    assert bal(period=0) == decimal.Decimal(1000)
    assert bal(period=1) == decimal.Decimal("950.00")
    assert bal(period=2) == decimal.Decimal("897.5000")
    assert bal(period=3) == decimal.Decimal("842.375000")
    assert bal(period=4) == decimal.Decimal("784.49375000")
    assert bal(period=5) == decimal.Decimal("723.7184375000")
    assert bal(period=10) == decimal.Decimal("371.10537322255859375000")
    # assert bal(period=15) == decimal.Decimal("0")


def test__interest_only_loan(
    interest_only_loan: loan_calcs.InterestOnlyLoan,
):
    """
    Test that an interest-only loan is generated correctly.
    """

    assert interest_only_loan.periodic_repayment == decimal.Decimal("50.00")

    def bal(period: int) -> decimal.Decimal:
        return interest_only_loan.calculate_balance_at_period(period)

    assert bal(period=0) == decimal.Decimal(1000)
    assert bal(period=1) == decimal.Decimal(1000)
    assert bal(period=2) == decimal.Decimal(1000)
