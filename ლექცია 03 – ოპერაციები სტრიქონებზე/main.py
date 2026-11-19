# print(int('123a'))    # ValueError: invalid literal for int() with base 10: '123a'

print(int('123'))           # 123

print(int(10.5))            # 10
print(int(10.95))           # 10

print(float(10), "\n")      # 10.0


# bool
print(bool(23))             # True
print(bool(-17))            # True
print(bool(0))              # False

print(bool(0.1))            # True
print(bool(0.0), "\n")      # False


# str to bool
print(bool("Python"))       # True
print(bool(" "))            # True
print(bool(""), "\n")       # False


# bool to numeric
print(int(True))            # 1
print(int(False), "\n")     # 0


# bool to str
print(str(True))            # 'True'
print(str(False))           # 'False