# temperature = 32

# if temperature >= 30:
#   print("It's hot today")


# temperature = 25

# if temperature >= 30:
#   print("It's hot today")


# temperature = 25

# if temperature >= 30:
#   print("It's hot today")

# print("We have some weather")


# temperature = 25

# # კარგი მაგალითი
# if temperature >= 30:
#   print("It's hot today")
# else:
#   print("It's cold today")


# # ცუდი მაგალითი
# if temperature >= 30:
#   print("It's hot today")
# if temperature < 30:
#   print("It's cold today")




# შეფასების გამოთვლა

# # სწორი მაგალითი
# score = 83

# if score >= 90:
#   grade = 'A'
# elif score >= 80:
#   grade = 'B'
# elif score >= 70:
#   grade = 'С'
# elif score >= 60:
#   grade = 'D'
# else:
#   grade = 'F'

# print("Grade:", grade)



# # არასწორი მაგალითი
# score = 83

# if score >= 60:
#     grade = 'D'
# elif score >= 70:
#     grade = 'C'
# elif score >= 80:
#     grade = 'B'
# elif score >= 90:
#     grade = 'A'
# else:
#     grade = 'F'

# print("Grade:", grade)



# # რა დაიბეჭდება?
# score = 83

# if score >= 90:
#   print("A")
# if score >= 80:
#   print("B")
# if score >= 70:
#   print("C")



# age = 22          # 17
# has_id = True     # False

# if age >=18 and has_id:
#   print("You can vote")
# else:
#   print("You can't vote")


# age = 22                  # 17
# has_id = True             # False
# has_certificate = True    # False

# if age >=18 and has_id and has_certificate:
#   print("You can vote")
# else:
#   print("You can't vote")




# print(True and True)
# print(True and False)
# print(True and True and False)


# print(True or True)
# print(True or False)
# print(True or True or False)
# print(False or False)


# is_admin = False      # True
# is_moderator = True   # False

# if is_admin or is_moderator:
#   print("You can delete this post")
# else:
#   print("You can't delete this post")



# print(not True)
# print(not False)

# is_raining = False      # True

# if not is_raining:
#   print("The weather is good")
# else:
#   print("The weather is bad")


# if is_raining:
#   print("The weather is bad")
# else:
#   print("The weather is good")


# name = input("Enter your name: ")

# if not name:
#     print("Please enter your name")
# else:
#     print(f'Hello {name}!')



# პრიორიტეტი: NOT, AND, OR

# age = 18
# country = "GE"
# # has_tiket = True
# has_tiket = False

# if age >= 18 and country == "GE" or country == 'US' and has_tiket:
#   print("You can enter")


# age = 18
# country = "GE"
# has_tiket = True

# if age > 17 and (country == "GE" or country == 'US') and has_tiket:
#   print("You can enter")
# else:
#   print("You can't enter")




# x = 15
# y = 10

# if x == y:
#   print("OK!")
# else:
#   print("NO!")    # NO!



# x = 15
# y = 10

# if not x == y:      #  if not (x == y)    # if x != y
#   print("OK!")
# else:
#   print("NO!")





# # აქ რა დაიბეჭდება?
# if not False:
#   print(True)
# else:
#   print(False)
  
# if not True:
#   print(True)
# else:
#   print(False)




# ჩადგმული if ოპერატორები

# age = 25
# has_id = True
# has_ticket = False

# if age > 17:
#   if has_id and has_ticket:
#     print("You can enter")
#   else:
#     print("You can't enter")
# else:
#   print("You are underage")


# შეიძლება ასეც ჩავწეროთ
# age = 17
# has_id = True
# has_ticket = True

# if age > 17 and has_id and has_ticket:
#   print("You can enter")
# else:
#   print("You can't enter")


# ჩადგმული `if .. else`-ების დეტალური ინფორმაციის ბეჭდვა
# age = 25                # 16
# has_id = True           # False
# has_ticket = True       # False

# if age > 17:
#   if has_ticket:
#     if has_id:
#       print("You can enter")
#     else:
#       print("You can't id")
#   else:
#     print("You haven't ticket")
# else:
#   print("You can't enter")






# age = 25                # 16
# has_id = True           # False
# has_ticket = True       # False

# if age > 17:
#   print("Your age is ok")
#   print("Second print from first if")

#   if has_ticket and has_id:
#     print("You can enter")
#   else:
#     print("You can't enter")

#   print("Third print from first if")
# else:
#   print("You are underage")





# # რა დაიბეჭდერბა?

# print(True and False or True)         # False or True   ===>  True
# print(True and (False or True))       # True and True   ===>  True
# print (True and (True and False))     # True and False  ===>  False
# print(not False and True)             # True and True   ===>  True