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

# i = 1
# total = 0     # accumulator variable

# while i < 6:
#   total += i
#   i += 1

# print("The total is", total)





# # უსასრულო ციკლი

# while True:
#   text = input("Pleace enter your text: ").strip().lower()

#   if text == "exit" or text == "quit":
#     print("Exiting...")

#     break




# # დავბეჭდოთ ფიფქები (მართკუთხა სამკუთხედი)

# i = 10

# while True:
#   if i < 1:
#     break

#   print('*' * i)

#   i -= 1    # i = i - 1


# # აქაც იგივე შედეგს ვღებულობთ
# # i = 10

# # while i > 0:
# #   print('*' * i)

# #   i -= 1




# # გავაკეთოთ ფიფქების ანიმაციური გამოტანა.
# # ყოველი სტრიქონის დაყოვნებით გამოტანა.

# import time

# i = 10

# while True:
#   if i < 1:
#     break

#   print('*' * i)

#   time.sleep(0.25)

#   i -= 1    # i = i – 1

#   # დაიბეჭდება ფიფქების სტრიქონი 0.25 წამიანი დაყოვნებით




# ოპერატორი continue

# i = 0

# while i < 5:    # 0<5      1<5      2<5      3<5      4<5
#   i += 1        # 1        2        3        4        5

#   if i == 3:    # 1 == 3   2 == 3   3 == 3   4 == 3   5 == 3
#     continue

#   print(i)      # 1        2                 4        5





# ახლა print(i) ავწიოთ if i == 3 ზემოთ

# i = 0

# while i < 5:
#   i += 1

#   print(i)

#   if i == 3:
#     continue




# 1-დან 20-ის ჩათვლით დავბეჭდოთ რიცხვები, რომელთა 3-ზე გაყოფისას ნაშთი ტოლია 2-ის.

# i = 1

# while i < 20:
#   i += 1

#   if i % 3 == 0 or i % 3 == 1:
#     continue
  
#   print(i)




# უსასრულო ციკლი. break და continue

# import time

# i = 10

# while True:
#   if i < 1:
#     break
#   elif i < 4:
#     continue

#   print(i)
#   print("sleep\n")

#   time.sleep(0.25)

#   i -= 1




'''
აქ i ცვლადი გახდება 3-ის ტოლი

elif i < 4:
  continue

elif-ის პირობა მუდმივად ჭეშარიტია (i-ის მნიშვნელობა არ იცვლება, სულ 3-ის ტოლია).
ამიტომ continue-ს წინ უნდა ჩავსვათ: i -= 1
'''

# import time

# i = 10

# while True:
#   if i < 1:
#     break
#   elif i < 4:
#     i -= 1
#     continue

#   print(i)
#   print("sleep\n")

#   time.sleep(0.25)

#   i -= 1





# dry-ს პრინციპი რომ არ დაირღვეს შეიძლება, ასე ჩავწეროთ

# import time

# i = 11

# while True:
#   i -= 1

#   if i < 1:
#     break
#   elif i < 4:
#     continue

#   print(i)
#   print("sleep\n")

#   time.sleep(0.25)





# while .. else

# from time import sleep

# i = 10

# while i > 0:
#   print(i)

#   sleep(0.35)

#   i -= 1
# else:
#   print("While end")

# print("Script end")




# ახლა ვნახოთ, როდესაც ციკლიდან გამოვალთ brake-ით

# from time import sleep

# i = 10

# while i > 0:
#   if i < 2:
#     break

#   print(i)

#   sleep(0.35)

#   i -= 1
# else:
#   print("While end")

# print("Script end")




# ჩადგმული while ციკლი – Nested while loops

# * * *
# * * *
# * * *
# * * *

# row = 1

# while row < 5:
#   col = 1

#   while col < 4:
#     print("* ", end='')

#     col += 1

#   print()   # new line

#   row += 1




# for ციკლი

# print('y' in 'Python')

# for ch in "Python programming":
#   print(ch)





# arr = [1, 2, 3, 4, 5, 6, 7]

# for i in arr:
#   print(i)




# for i in range(5):    # 0 1 2 3 4
#   print(i)



# for i in range(5):    # 0 1 2 3 4
#   print(i, end=' ')

# print()





# for i in range(1, 11):
#   print(i, end=' ')

# print()






# for i in range(4, 15, 3):   # 4 7 10 13
#   print(i, end=' ')

# print()





# # დავბეჭდოთ 0-დან 10-მდე ლუწი რიცხვები
# for i in range(0, 10, 2):
#   print(i, end=' ')

# print("\n")


# # დავბეჭდოთ 1-დან 10-მდე კენტი რიცხვები
# for i in range(1, 10, 2):
#   print(i, end=' ')

# print("\n")


# # დავბეჭდოთ 1-დან 15-მდე ყველა რიცხვი 3-ის ბიჯით
# for i in range(1, 15, 3):
#   print(i, end=' ')

# print("\n")


# # დავბეჭდოთ 37-დან 21-მდე ყველა რიცხვი კლებადობის მიხედით, ბიჯი იგულისხმება -1
# for i in range(37, 21, -1):
#   print(i, end=' ')

# print("\n")


# for i in range(58, 29, -4):
#   print(i, end=' ')

# print()





# The Accumulator Pattern with for

# total = 0

# for i in range(1, 21):
#   total += i

# print("Total =", total)



# # break ოპერატორი

# for num in range(1, 11):
#   print(num)

#   if num == 5:
#     break





# # რა განსხვავებაა ზედა და ქვედა კოდს შორის?

# for num in range(1, 11):
#   if num == 5:
#     break

#   print(num)





# # რას დაბეჭდავს და რა შემთხვევაში გაჩერდება ციკლი?

# for i in range(1, 20):
#   print(i)
#   break






# # ლუწი რიცხვების დაბეჭდვა range() ფუნქციის გამოყენების გარეშე

# for i in range (1, 11):
#   if i % 2 == 0:
#     print(i)




# continue ოპერატორი

#  დავბეჭდოთ ლუწი რიცხვები continue-ს გამოყენებით [0, 20]

# for i in range(21):
#   if i % 2 != 0:      # if i % 2 == 1:    if i % 2:
#     continue

#   print(i, end=' ')

# print()




# რა დაიბეჭდება?

# for i in range(10):
#   continue

#   print(i)
#   print(i ** 2)




# ამ შემთხვევაში?

# for i in range(10):
#   print(i)
  
#   continue

#   print(i ** 2)





# დავბეჭდოთ 1-დან 20-ის ჩათვლით რიცხვების ჯამი 10-სა და 11-ის გამოტოვებით

# s = 0

# for i in range(1, 21):
#   if i == 10 or i == 11:    # if i in range(10, 12)
#     continue
  
#   s += i

# print(s)





# continue-ს გამოყენებით დავბეჭდოთ რიცხვები 1-დან 20-ის ჩათვლით, გარდა რიცხვებისა დიაპაზონით [10, 15]

# for i in range(1, 21):
#   if 10 <= i <= 15:   # if i >= 10 and i <= 15:   if i in range(10, 16):
#     continue

#   print(i, end=' ')

# print()





# იგივე ამოცანა continue-ს გარეშე

# for i in range(1, 21):
#   if i < 10 or i > 15:
#     print(i, end=' ')

# print("\n")


# # not
# for i in range(1, 21):
#   if not (i < 10 or i > 15):
#     print(i, end=' ')

# print("\n")


# # დიაპაზონი [10, 16]
# for i in range(1, 21):
#   if 9 < i < 16:
#     print(i, end=' ')

# print("\n")


# # range()
# for i in range(1, 21):
#   if i in range(10, 16):
#     print(i, end=' ')

# print("\n")


# # not in range()
# for i in range(1, 21):
#   if i not in range(10, 16):
#     print(i, end=' ')

# print()




# ჩადგმული for ციკლი – Nested for loops

# * * *
# * * *
# * * *
# * * *

# for row in range(4):
#   for col in range(3):
#     print("*", end=' ')

#   print()




for i in range(1, 6):
  print(i)
  
  if i == 3:
    continue
