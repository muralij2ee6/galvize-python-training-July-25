# Exception Handling Demo



# exception handling in python is done using try/except blocks

#indexError - trying to access an index that doesn't exist 
# assertionError - raised when an assert statement fails
# attiributeError - trying to access an attribute that doesn't exist
# importError - trying to import a module that doesn't exist
# typeError - trying to perform an operation on a value of the wrong type
# valueError - trying to convert a value to a type that is not compatible
# zeroDivisionError - trying to divide by zero
# nameError - trying to access a variable that doesn't exist

class MyCustomError(Exception):
    """Custom exception for demonstration purposes."""
    pass

class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    def __init__(self, number):
        super().__init__(f"Negative number error: {number} is not allowed.")
        self.number = number
    


def fifty_by(number):
    # if number == 0:
    #     raise ZeroDivisionError("Cannot divide by zero!")
    try:
        if number == 1:
            raise MyCustomError
        if number < 0:
            raise NegativeNumberError(number)
        return 50 / number
    except ZeroDivisionError: 
        return "Error: Cannot divide by zero!"
    except MyCustomError:
        return "in execpt statement Error: Number cannot be 1!"
    except NegativeNumberError:
        return f"Error: {number} is a negative number!"

   

print(fifty_by(0))
print(fifty_by(1))
print(fifty_by(-5))

# print(help(ZeroDivisionError))

# banking 

# class InsufficientFundsError(Exception):
#     """Custom exception for insufficient funds."""
#     # constructo init 
#     # balance, amount 

#     # method to make a message 

#     # method for deficit value 
#     # return how much amount mmore money is needed to cover the deficit
#     # self.amount - self.balance

#     # suggested action method 
#     # consider depositing more money or withdrawing less


# except InsufficientFundsError as e:: 
#     print(f"Error: {e} {e.deficit_value()} is needed to cover the deficit. Consider depositing more money or withdrawing less.")