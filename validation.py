"""
validation.py
Handles input validation for the Mini Bank Account Management System.
"""


def validate_name(name):
    """Check that a name contains only letters and spaces."""
    if not name.strip():
        return False, "Name cannot be empty."
    if not all(part.isalpha() for part in name.split()):
        return False, "Name should contain only letters."
    return True, ""


def validate_account_number(acc_no, existing_numbers):
    """Check that an account number is exactly 6 digits and unused."""
    if not acc_no.isdigit() or len(acc_no) != 6:
        return False, "Account number must be exactly 6 digits."
    if acc_no in existing_numbers:
        return False, "This account number already exists."
    return True, ""


def validate_pin(pin):
    """Check that a PIN is exactly 4 digits."""
    if not pin.isdigit() or len(pin) != 4:
        return False, "PIN must be exactly 4 digits."
    return True, ""


def validate_amount(amount_str):
    """Check that an amount is a positive number."""
    try:
        amount = float(amount_str)
    except ValueError:
        return False, "Amount must be a number."
    if amount <= 0:
        return False, "Amount must be greater than zero."
    return True, ""