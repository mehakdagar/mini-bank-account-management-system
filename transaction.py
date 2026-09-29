"""
transaction.py
Handles deposits and withdrawals for an account.
"""

from validation import validate_amount


def deposit(account):
    """Add a validated amount to the account's balance."""
    if account is None:
        print("No account selected. Search for an account first.")
        return

    print("\n--- Deposit ---")
    while True:
        amount_str = input("Enter amount to deposit: ").strip()
        is_valid, message = validate_amount(amount_str)
        if is_valid:
            break
        print(f"  Invalid input: {message}")

    amount = float(amount_str)
    account["balance"] += amount
    print(f"Rs. {amount:.2f} deposited. New balance: Rs. {account['balance']:.2f}")


def withdraw(account):
    """Verify the PIN, then subtract a validated amount if funds allow."""
    if account is None:
        print("No account selected. Search for an account first.")
        return

    print("\n--- Withdraw ---")
    pin = input("Enter your 4-digit PIN: ").strip()
    if pin != account["pin"]:
        print("Incorrect PIN. Withdrawal cancelled.")
        return

    while True:
        amount_str = input("Enter amount to withdraw: ").strip()
        is_valid, message = validate_amount(amount_str)
        if is_valid:
            break
        print(f"  Invalid input: {message}")

    amount = float(amount_str)
    if amount > account["balance"]:
        print(f"Insufficient balance. Current balance is Rs. {account['balance']:.2f}.")
        return

    account["balance"] -= amount
    print(f"Rs. {amount:.2f} withdrawn. New balance: Rs. {account['balance']:.2f}")