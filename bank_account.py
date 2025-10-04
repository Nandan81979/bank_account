# bank_account.py

# Ask user for initial balance
initial_balance = float(input("Enter your initial balance: "))

# Ask for deposit amount
deposit = float(input("Enter deposit amount: "))

# Update balance
balance = initial_balance + deposit
print("Updated Balance after deposit: ₹", balance)

# Ask for withdrawal
withdraw = float(input("Enter withdrawal amount: "))

if withdraw > balance:
    print("Insufficient balance!")
else:
    balance -= withdraw
    print("Updated Balance after withdrawal: ₹", balance)