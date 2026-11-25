# username = input("Please enter your name: ")

# if not username:
#   print("Please enter your name: ")
# else:
#   print(f"Hello {username}")




# while ციკლი

# count = 0

# while count < 5:  # 0 < 5   1 < 5   2 < 5   3 < 5   4 < 5   5 < 5: False  ===> while-ის დასასრული
#   print(count)    # 0 1 2 3 4

#   count += 1      # 0 1 2 3 4 5



# i = 5

# while i > 0:
#   print(f"Step {i}. Hello friends!...")

#   i -= 1




# ციკლის გაჩერება – Sentinel-Controlled Loop

# total = 0
# number = 0

# while number != -1:
#   number = eval(input("Enter a number (-1 to stop): "))

#   if number != -1:
#     total += number

# print("Total:", total)



# password = ''

# while password != "Python":
#   password = input("Please enter your password: ")

# print("\nYou entered the correct password")




# ახალ მომხმარებელს მივცეთ მცდელობების საშუალება:
# თუ სამჯერ შეიყვანა არასწორი პაროლი პროგრამამ შესაბამისი შეტყობინა გამოიტანოს და გაჩერდეს

# password = ''
# tries = 1   # 0

# while password != "Python" and tries < 4:   # 3
#   password = input("Please enter your password: ")

#   tries += 1




# ციკლში and შევცვალოთ or-ით

# password = ''
# tries = 1   # 0

# while password != "Python" or tries < 4:   # 3
#   password = input("Please enter your password: ")

#   tries += 1




# პროგრამაში გავითვალისწინოთ მცდელობების ამოწურვის შემთხვევაში შესაბამისი შეტყობინების ბეჭდვა.

# password = ''
# tries = 1   # 0

# while password != "Python" and tries < 4:   # 3
#   password = input("Please enter your password: ")

#   tries += 1

#   if tries > 3:
#     print("\nYou entered the wrong password 3 times")
#   else:
#     print("\nYou entered the correct password")




# ვალიდაცია – Validation Loop

# age = 0

# while age < 1 or age > 120:
#   age = int(input("Please enter valid age(0-120): "))

# print("\nAccepted age:", age)





# The Accumulator Pattern

i = 1
total = 0

while i < 6:
  total += i
  i += 1

print("The total is", total)