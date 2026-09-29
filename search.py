"""
search.py
Handles finding an account by account number and listing all accounts.
"""

from account import display_account


def search_account(accounts, acc_no):
    """Return the account dict matching acc_no, or None if not found."""
    for account in accounts:
        if account["account_number"] == acc_no:
            return account
    return None


def search_and_display(accounts):
    """Prompt for an account number and display the matching account, if any."""
    print("\n--- Search Account ---")
    acc_no = input("Enter account number: ").strip()
    account = search_account(accounts, acc_no)
    if account:
        display_account(account)
    else:
        print(f"No account found with number '{acc_no}'.")
    return account


def display_all_accounts(accounts):
    """Print a summary table of every account in the bank."""
    print("\n--- All Accounts ---")
    if not accounts:
        print("No accounts have been created yet.")
        return

    print(f"{'Acc No':<10}{'Name':<20}{'Balance':<15}")
    print("-" * 45)
    for a in accounts:
        print(f"{a['account_number']:<10}{a['name']:<20}{'Rs. ' + format(a['balance'], '.2f'):<15}")