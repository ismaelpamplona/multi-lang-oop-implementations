from datetime import datetime

import pytest
from bank_account import BankAccount


def test_create_valid_bank_account():
    account = BankAccount("12345", "savings", 1000.0)
    assert account.account_number == "12345"
    assert account.account_type == "savings"
    assert account.balance == 1000.0
    assert account.transactions == []


def test_create_invalid_account_number():
    with pytest.raises(ValueError, match="Account number must be a non-empty string."):
        BankAccount("", "savings", 1000.0)


def test_create_invalid_account_type():
    with pytest.raises(
        ValueError, match="Account type must be either 'checking' or 'savings'."
    ):
        BankAccount("12345", "investment", 1000.0)


def test_create_invalid_balance():
    with pytest.raises(ValueError, match="Balance must be a non-negative number."):
        BankAccount("12345", "savings", -50.0)


def test_deposit_valid_amount():
    account = BankAccount("12345", "checking", 500.0)
    account.deposit(200.0)
    assert account.balance == 700.0
    assert len(account.transactions) == 1
    assert "Deposited: 200.0" in account.transactions[0]


def test_deposit_invalid_amount():
    account = BankAccount("12345", "checking", 500.0)
    with pytest.raises(ValueError, match="Amount must be a non-negative number."):
        account.deposit(-100.0)


def test_withdraw_valid_amount():
    account = BankAccount("12345", "checking", 500.0)
    account.withdraw(200.0)
    assert account.balance == 300.0
    assert len(account.transactions) == 1
    assert "Withdraw: 200.0" in account.transactions[0]


def test_withdraw_insufficient_funds():
    account = BankAccount("12345", "checking", 100.0)
    with pytest.raises(ValueError, match="Insufficient balance."):
        account.withdraw(200.0)


def test_withdraw_invalid_amount():
    account = BankAccount("12345", "checking", 500.0)
    with pytest.raises(ValueError, match="Amount must be a non-negative number."):
        account.withdraw(-50.0)


def test_apply_interest_to_savings():
    account = BankAccount("12345", "savings", 1000.0)
    account.apply_interest(5)  # 5% interest
    assert account.balance == 1050.0
    assert len(account.transactions) == 1
    assert "Interest Applied: 50.0 (5%)" in account.transactions[0]


def test_apply_interest_to_checking():
    account = BankAccount("12345", "checking", 1000.0)
    with pytest.raises(
        ValueError, match="Interest can only be applied to savings accounts."
    ):
        account.apply_interest(5)


def test_apply_interest_invalid_rate():
    account = BankAccount("12345", "savings", 1000.0)
    with pytest.raises(
        ValueError, match="Interest rate must be a non-negative number."
    ):
        account.apply_interest(-5.0)
