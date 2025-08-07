def add(a, b):
    return a + b

print("this runs no matter what")

print(__name__=="__main__")
print(__name__)


if __name__ == "__main__":
    print("this proves that only this file is running directly - not as an imported module from another file.")
    print("2 + 3 =", add(2, 3))