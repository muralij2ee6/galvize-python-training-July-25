class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute
        self.__transaction_history = []   # Private attribute

    def deposit(self, amount):
        """Public method to deposit money"""
        if self.__validate_amount(amount):
            self.__balance += amount
            self.__log_transaction(f"Deposit: +${amount}")
            return f"✅ Deposited ${amount}. New balance: ${self.__balance}"
        return "❌ Invalid deposit amount"

    def withdraw(self, amount):
        """Public method to withdraw money"""
        if self.__validate_amount(amount) and self.__check_sufficient_funds(amount):
            self.__balance -= amount
            self.__log_transaction(f"Withdrawal: -${amount}")
            return f"✅ Withdrew ${amount}. New balance: ${self.__balance}"
        return "❌ Invalid withdrawal or insufficient funds"

    def get_balance(self):
        """Public method to check balance"""
        return f"💰 Balance for {self.account_holder}: ${self.__balance}"

    def __validate_amount(self, amount):
        """Private method to validate amount is positive"""
        return amount > 0

    def __check_sufficient_funds(self, amount):
        """Private method to check if enough funds exist"""
        return amount <= self.__balance

    def __log_transaction(self, transaction):
        """Private method to record transactions"""
        self.__transaction_history.append(transaction)
        print(f"📝 Transaction logged: {transaction}")

    def get_statement(self):
        """Public method to get transaction history"""
        statement = "\n".join(self.__transaction_history)
        return f"📊 Account Statement:\n{statement}"


# Usage Example
account = BankAccount("John Doe", 1000)

print(account.deposit(500))      # ✅ Deposited $500. New balance: $1500
print(account.withdraw(200))     # ✅ Withdrew $200. New balance: $1300
print(account.withdraw(2000))    # ❌ Invalid withdrawal or insufficient funds
print(account.get_balance())     # 💰 Balance for John Doe: $1300

# Trying to access private methods/attributes directly (won't work)
try:
    print(account.__balance)          # Fails
except AttributeError as e:
    print(f"🔒 Access denied: {e}")

try:
    account.__validate_amount(100)    # Fails
except AttributeError as e:
    print(f"🔒 Access denied: {e}")

# Get statement through proper public interface
print(account.get_statement())