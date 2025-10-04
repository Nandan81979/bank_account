# bank_account.py

# Ask user for initial balance
initial_balance = float(input("Enter your initial balance: "))

# Ask for deposit amount
deposit = float(input("Enter deposit amount: "))

# Update balance
balance = initial_balance + deposit

print("Updated Balance after deposit: ₹", balance)