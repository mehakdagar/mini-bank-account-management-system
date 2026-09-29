# Mini Bank Account Management System

A console-based bank account management system built in Python, developed as a VITyarthi mini project.

## Overview
The Mini Bank Account Management System lets a user create accounts, deposit and withdraw money, check balances, and view account details, all through a menu-driven command-line interface.

## Features
- Create a new account with a validated name, 6-digit account number, and 4-digit PIN
- Deposit money into an account
- Withdraw money after PIN verification, with an insufficient-balance check
- Check the current balance of an account
- Display full details of a single account (PIN masked)
- Display a summary of every account in the system

## Technologies Used
- Python 3 (standard library only, no external packages)

## Project Structure
```
Mini-Bank-Account-System/
├── main.py
├── account.py
├── search.py
├── transaction.py
├── balance.py
├── validation.py
├── README.md
└── statement.md
```

## How to Install & Run
1. Make sure Python 3 is installed.
2. Clone this repository:
   ```
   git clone <your-repo-url>
   ```
3. Move into the project folder:
   ```
   cd Mini-Bank-Account-System
   ```
4. Run the program:
   ```
   python main.py
   ```

## Instructions for Testing
- Choose option 1 and create an account. Try a 5-digit account number or a duplicate number to see validation in action.
- Choose option 2 to search by the account number you just created.
- Choose option 3 to deposit money, then option 5 to confirm the balance updated.
- Choose option 4 to withdraw money. Try the wrong PIN once to see it rejected, then the correct PIN with an amount larger than the balance to see the insufficient-funds message.
- Choose option 6 to view full account details, and option 7 to see every account listed together.

## Screenshots
Add screenshots of the program running here once you have tested it (e.g. successful_output.png, search_account.png, account_details.png). 
