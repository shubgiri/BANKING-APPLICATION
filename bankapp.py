class Bank:
    def __init__(self, name, branch, account_no, age, mob, year, rate, loan_amount):
        self.name, self.branch, self.account_no, self.age, self.mob = name, branch, account_no, age, mob
        self.amount, self.loan_amount, self.year, self.rate = 10000, loan_amount, year, rate

    def enquiry(self):
        print(f"Customer Details:\nBank Name: {self.name}\nBranch Name: {self.branch}\n"
              f"Account Number: {self.account_no}\nAge: {self.age}\nMobile Number: {self.mob}")

    def deposit(self, amount):
        self.amount += amount
        print(f"Amount Successfully Deposited: Rs. {amount}")
        self.display()

    def withdraw(self, amount):
        if self.amount >= amount + 1000:
            self.amount -= amount
            print("Amount Successfully Withdrawn")
            self.display()
        else:
            print("Insufficient Balance. You must maintain a minimum balance of Rs. 1000")

    def display(self):
        print(f"Account Holder: {self.name} (Account Number: {self.account_no})\nCurrent Balance: Rs. {self.amount}")

    def simple_interest(self):
        return (self.year * self.rate * self.loan_amount) / 100

    def apply_for_loan(self):
        loan_amount = int(input("Enter the loan amount: "))
        user_age = int(input("Enter your age: "))

        if user_age > 18:
            self.year, self.rate = int(input("Enter the number of loan years: ")), float(
                input("Enter the rate of interest: "))
            simple_interest = self.simple_interest()
            print(f"Congratulations! Your loan of Rs. {loan_amount} has been approved.")
            print(f"The simple interest is: {simple_interest}")
            self.amount += loan_amount
        else:
            print("Sorry, you are not eligible for a loan at this time.")


def handle_deposit(bank):
    amount = int(input("Enter the amount for deposit: "))
    bank.deposit(amount)


def handle_withdraw(bank):
    amount = int(input("Enter the amount for withdrawal: "))
    bank.withdraw(amount)


def handle_action(bank, action):
    actions = {
        '1': bank.enquiry,
        '2': handle_deposit,
        '3': handle_withdraw,
        '4': bank.display,
        '5': bank.apply_for_loan
    }

    selected_action = actions.get(action)
    if selected_action:
        if action == '2' or action == '3':
            selected_action(bank)
        else:
            selected_action()
    else:
        print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    print("********** Welcome to BOI internet services **********")
    b = Bank("BOI", "Mumbai", 123525, 22, 1111111111, 10, 8, 1000000)
    user_choice = input("\n1. Enquiry\n2. Deposit\n3. Withdraw\n4. Display Balance\n5. Apply for Loan\n~select one option to proceed further:")
    handle_action(b, user_choice)
