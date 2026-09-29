"""
account.py
Handles creating new accounts and displaying a single account's details.
"""

from validation import validate_name, validate_account_number, validate_pin, validate_amount


def get_valid_input(prompt, validator, *extra_args):
    """Keep asking until the entered value passes the validator."""
    while True:
        value = input(prompt).strip()
        is_valid, message = validator(value, *extra_args)
        if is_valid:
            return value
        print(f"  Invalid input: {message}")


def create_account(accounts):
    """Collect account details from the user and open a new account."""
    print("\n--- Create New Account ---")
    existing_numbers = [a["account_number"] for a in accounts]

    name = get_valid_input("Account holder's name: ", validate_name)
    acc_no = get_valid_input("Choose a 6-digit account number: ", validate_account_number, existing_numbers)
    pin = get_valid_input("Set a 4-digit PIN: ", validate_pin)

    opening_deposit = 0.0
    deposit_str = input("Opening deposit amount (press Enter to skip): ").strip()
    if deposit_str:
        is_valid, message = validate_amount(deposit_str)
        if is_valid:
            opening_deposit = float(deposit_str)
        else:
            print(f"  Skipped opening deposit: {message}")

    new_account = {
        "account_number": acc_no,
        "name": name,
        "pin": pin,
        "balance": opening_deposit,
    }
    accounts.append(new_account)
    print(f"\nAccount created for {name}. Account number: {acc_no}. "
          f"Opening balance: Rs. {opening_deposit:.2f}")
    return new_account


def display_account(account):
    """Print one account's details, with the PIN masked."""
    print("\n----- ACCOUNT DETAILS -----")
    print(f"Account Number : {account['account_number']}")
    print(f"Holder Name    : {account['name']}")
    print(f"PIN            : ****")
    print(f"Balance        : Rs. {account['balance']:.2f}")