# ===============================================
# მთელი და ათწილადი რიცზვები – int / float
# ===============================================

# print(10)
# print(10.5)

# print(type(10))
# print(type(10.5))


# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 ** 3)

# print()

# print(10 / 3)       # ჩვეულებრივი გაყოფა  ===>  float
# print(10 // 3)      # მთელზე გაყოფა  ===>  int
# print(10 % 3)       # ნაშთი  ===>  int
# print(10 % 2)         # ლუწი / კენტი
# print(11 % 2)         # ლუწი / კენტი



# print(10 + 5.4)
# print(10 - 5.4)
# print(10 * 5.4)
# print(10.5 * 5.5)
# print(5 * 5.0)
# print(0.1 + 0.1)
# print(0.1 + 0.2, "\n")

# print(16 ** 0.5)
# print(16 ** (1/2))
# print(8 ** (1/3))
# print(8 ** (2/3))




# x1 = -b / 2 * a
# x1 = -b / (2 * a)




# print(5 // 2)             # 2.5  ===> მრგვალდება ქვემოთა მხარეს
# print(5 // -2, "\n")      # -2.5 ===> მრგვალდება ქვემოთა მხარეს

# print(5 % 2)
# print(5 % -2)        # 5 - 6 = -1
# print(10 % -3)       # 10 - 12 = -2
# print(10 % -6)       # 10 - 12 = -4
# print(10 % -7)       # 10 - 14 = -4
# print(10 % -8)       # 10 - 16 = -6





# ===============================================
# სტრიქონები – Strings / str
# ===============================================

# print("Python is fun")
# print('Python is fun', "\n")

# print(type("Python is fun"), "\n")

# print("Python", "Java", "C++")




# ===============================================
# Booleab / bool
# ===============================================

# print(True)
# print(False, "\n")

# print(10 > 5)
# print(10 < 5)
# print(7 >= 3)
# print(6 <= 13)
# print(10 == 5)
# print(10 != 5)





# ===============================================
# NoneType / None
# ===============================================

# print(None)
# print(type(None), "\n")

# print(5 + None)




# ===============================================
# ცვლადები – Variables
# ===============================================

# num1 = 5
# num2 = 2

# print(num1 + num2)
# print(num1 - num2, "\n")

# count = 3
# print(count)

# count = count - 1
# print(count)

# count -= 1
# print(count)





### ცვლადების სახელები

# არასწორი სახელები – შეცდომა / ERROR
# user age = 28
# user-age = 15


# ცვლადის სწპრი სახელები
# user_age = 54         # snake_case
# userAge = 20          # camelCase
# FirstName = 'Alex'    # PascalCase


# აკრძალული სახელები
# import keyword

# print(keyword.kwlist)




# ===============================================
# მონაცემთა ტიპოების გარდაქმნა – Casting
# ===============================================

# num1 = input("Enter a num1: ")
# num2 = input("Enter a num2: ")

# print(num1, num2)
# print(num1 + num2, "\n")

num1 = eval(input("Enter a num1: "))
num2 = eval(input("Enter a num2: "))

# num1 = eval(num1)
# num2 = eval(num2)

print(num1, num2)
print(num1 + num2, "\n")

print(type(num1))
print(type(num2))