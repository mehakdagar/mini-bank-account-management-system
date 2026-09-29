"""
main.py
Mini Bank Account Management System - main menu and program entry point.
"""
1
from account import create_account, display_account
from search import search_and_display, display_all_accounts
from transaction import deposit, withdraw
from balance import check_balance


def print_menu():
    print("\n===== MINI BANK ACCOUNT MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Search Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Display Account Details")
    print("7. Display All Accounts")
    print("8. Exit")


def main():
    accounts = []
    last_account = None

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            last_account = create_account(accounts)

        elif choice == "2":
            last_account = search_and_display(accounts)

        elif choice == "3":
            deposit(last_account)

        elif choice == "4":
            withdraw(last_account)

        elif choice == "5":
            check_balance(last_account)

        elif choice == "6":
            if last_account:
                display_account(last_account)
            else:
                print("Search for an account first (option 2).")

        elif choice == "7":
            display_all_accounts(accounts)

        elif choice == "8":
            print("Exiting Mini Bank Account Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()