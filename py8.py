class BankDatabase():
    def __init__(self):
        # Nested dictionary mapping customer account details
        self.accounts = {
            "101": {
                "name": "Sarthak Mahurkar", 
                "account_type": "Savings", 
                "balance": 45000.0,
                "pan": "ABC1234"
            },
            "102": {
                "name": "Aryan Patil", 
                "account_type": "Current", 
                "balance": 12000.0,
                "pan": "DEF5678"
            },
            "103": {
                "name": "Ojaswi Dhuliya", 
                "account_type": "Savings", 
                "balance": 85000.0,
                "pan": "GHI8912"
            }
        }
        
    def get_all_accounts(self):
        return self.accounts

class SavingsAccount(BankDatabase):
    def __init__(self, account_number):
        self.is_valid = False
        self.account_number = account_number
        super().__init__()  # Triggers parent constructor to load database tracking records
        self.db = self.get_all_accounts()
        
        # Direct lookup logic to verify if account exists instantly
        if self.account_number in self.db:
            print(f"\nWelcome back, {self.db[self.account_number]['name']}!")
            print("-" * 60)
            self.is_valid = True
            
    def process_withdrawal(self, amount):
        customer = self.db[self.account_number]
        
        # Security validation gates checking funds limits
        if amount > customer["balance"]:
            print(f"Transaction Failed! Insufficient balance.")
            print(f"Available Balance: ₹{customer['balance']:.2f}")
            return False
        else:
            customer["balance"] -= amount  # Mutates data grid record state smoothly
            print(f"₹{amount:.2f} Debited Successfully!")
            print(f"Updated Account Balance: ₹{customer['balance']:.2f}")
            return True

# --- Main Runtime Loop Execution ---
print("=" * 60)
print("----------------- NATIONAL BANK -----------------")
print("=" * 60)
action = "yes"

while action.lower() != "no":
    print("-" * 60)
    acc_no = input("Please enter your Account Number: ").strip().upper()
    print("-" * 60)
    
    # Initialize the child object passing parameter properties
    session = SavingsAccount(acc_no)
    
    if session.is_valid:
        print("1. Check Account Overview")
        print("2. Withdraw Cash")
        choice = input("Select an operation (1/2): ").strip()
        print("-" * 60)
        
        customer_records = session.get_all_accounts()
        profile = customer_records[acc_no]
        
        if choice == "1":
            print("\t\tACCOUNT SUMMARY RECEIPT \n")
            print(f" HOLDER NAME   : {profile['name']}")
            print(f" ACCOUNT TYPE  : {profile['account_type']}")
            print(f" PAN ID LOGGED : {profile['pan']}")
            print("-" * 60)
            print(f" CURRENT BALANCE : ₹{profile['balance']:.2f}")
            print("-" * 60)
            
        elif choice == "2":
            withdraw_amt = float(input("Enter amount to withdraw: ₹"))
            print("-" * 60)
            session.process_withdrawal(withdraw_amt)
            
        else:
            print("Invalid Choice Selected!")
            
    else:
        print("Access Denied: Invalid Account Number entered! \n")
        
    action = input("\nDo you want to perform another transaction? (yes/no): ").strip()

else:
    print("\n================ Thank you for banking with us! ================")