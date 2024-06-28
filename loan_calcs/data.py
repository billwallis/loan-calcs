"""
All handy enums and module functions that can be used throughout the package.
"""

from __future__ import annotations

import enum


class RepaymentInterval(enum.Enum):
    """The interval over which the repayments are made."""

    YEARLY = enum.auto()
    MONTHLY = enum.auto()
    WEEKLY = enum.auto()
    DAILY = enum.auto()


class RepaymentFrequency(enum.Enum):
    """The frequency with which the repayments are made."""

    def __init__(
        self,
        repayment_unit: RepaymentInterval,
        repayment_frequency: int,
        total_repayments: int,
    ):
        """
        Defines a repayment schedule.

        :param repayment_unit: The calendar interval over which repayments are made.
        :param repayment_frequency: The number of calendar intervals between repayments.
        :param total_repayments: The total number of repayments.
        """
        self.repayment_unit = repayment_unit
        self.repayment_frequency = repayment_frequency
        self.total_repayments = total_repayments


class RepaymentType(enum.Enum):
    """
    Loan repayment types which determines the values of each repayment.

    Check the documentation of the corresponding loan objects for explanations
    of their differences.
    """

    FIXED_REPAYMENT = enum.auto()
    FIXED_PRINCIPAL = enum.auto()
    INTEREST_ONLY = enum.auto()


class InterestRateType(enum.Enum):
    """
    Loan interest rate types.

    - VARIABLE: A variable rate can change over the lifetime of the loan. This
      is usually when the interest rate is tied to a benchmark rate that also
      changes over time, such as the Bank of England rate.

    - FIXED: A fixed rate does not change over the lifetime of the loan.
    """

    VARIABLE = enum.auto()
    FIXED = enum.auto()


class InterestApplyMethod(enum.Enum):
    """
    Whether the interest is applied before or after the repayment.
    """

    BEFORE = 0
    AFTER = 1
