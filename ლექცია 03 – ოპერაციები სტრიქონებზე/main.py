# print(int('123a'))    # ValueError: invalid literal for int() with base 10: '123a'

# print(int('123'))           # 123

# print(int(10.5))            # 10
# print(int(10.95))           # 10

# print(float(10), "\n")      # 10.0


# # bool
# print(bool(23))             # True
# print(bool(-17))            # True
# print(bool(0))              # False

# print(bool(0.1))            # True
# print(bool(0.0), "\n")      # False


# # str to bool
# print(bool("Python"))       # True
# print(bool(" "))            # True
# print(bool(""), "\n")       # False


# # bool to numeric
# print(int(True))            # 1
# print(int(False), "\n")     # 0


# # bool to str
# print(str(True))            # 'True'
# print(str(False))           # 'False




# ==============================================
# სტრიქონის შექმნა
# ==============================================

# word1 = "Python"
# word2 = 'Python'
# word3 = '''Python'''
# word4 = """Python"""

# print(word1)
# print(word2)
# print(word3)
# print(word4, "\n")

# print(word1[0])
# print(word1[1])
# print(word1[-1])
# # print(word1[10])     # IndexError: string index out of range
# print(word1[-2])




# ==============================================
# ჭრები სტრიქონში – String Slicing / slice
# ==============================================

# [start:stop:step]   დიაპაზონი

# text = "python is funny"

# print(text[1:3])
# print(text[2:11:3])
# print(text[0:4])
# print(text[:4])
# print(text[3:])
# print(text[3:-1])
# print(text[2:10:2])
# print(text[2::2])
# print(text[::2], "\n")

# print(text[10:5:-1])
# print(text[10:5:-2])
# print(text[::-1])
# print(text[::-3])
# print(text[-5:-2])
# print(text[-5:-2:-1])     # ცარიელი სტრიქონი




# ახლა, ჩვენი ამოცანაა შევცვლაოთ python is funny ტექსტი Python is Funny-ით.

# text = "python is funny"    # "Python is Funny"
# print(text)
# print(id(text), "\n")

# text = 'P' + text[1:]

# print(text)
# print(id(text))



# text = "python is funny"    # "Python is Funny"
# sub_text_index = text.find('funny')

# text = 'P' + text[1:sub_text_index] + 'F' + text[sub_text_index+1:]

# print(text)

# # text = 'P' + text.replace(' ', ' P')
# # print(text)     # PPython Pis PFunny




# სტრიქონის კოპირება
# text1 = "python is funny"

# text2 = text1

# print(text1, id(text1))
# print(text2, id(text2), "\n")

# text2 = 'P' + text2[1:]
# print(text1, id(text1))
# print(text2, id(text2))


# # text2 = text1[:]   ===>  კოპირდება text ცვლადის შიგთავსი, მაგრამ არა სტრიქონების შემთხვევაში
# #                          ამ შემთხვევაში ორივე ცვლადი მიუთითებს ერთსა და იმავე ობიექტს



# სტრიქონების კონკატენაცია '+'
# text = "Python"
# print(text, id(text), "\n")

# # text = text + ' Programming'
# text += ' Programming'
# print(text, id(text))




# ==============================================
# სტრიქონის მეთოდები
# ==============================================

# text = 'Python is programming language'

# print(text.upper(), "\n")
# print(text.lower(), "\n")
# print(text.capitalize(), "\n")
# print(text.title(), "\n")

# print(text.count('a'), text.count('lan'), "\n")

# print(text.find('m'))
# print(text.find('k'))
# print(text.find('programming'))
# print(text.find('hon is'))
# print(text.find('hon Is'), "\n")

# print(text.index('l'))
# print(text.index('ing lan'))
# print(text.index('K'))          # ValueError: substring not found



# # მეთოდი .replace()
# st = "1 2 3 4 5 6 7 8 9 0"
# print(st.replace('5', 'five'))

# st = "1 2 3 4 5 6 7 8 9 0 5 5 4 8"
# print(st.replace('5', 'five', 2), "\n")


# # სტრიქონის სიგრძე (სმბოლოების რაოდენობა) – ფუნქცია len()
# st = "My first commit"
# print(len(st), "\n")


# მეთოდები: .isalpha(), .isdigit(), .isalnum()
# st = "Language"
# print(st.isalpha())
# print("Hello world".isalpha())
# print("Hello,".isalpha(), "\n")

# print("5.6".isdigit())
# print("56".isdigit())
# print("-56".isdigit(), "\n")

# st = 'John Walker is 52 years old'
# print(st.isalnum())
# print("125zsds".isalnum(), "\n")


# # მეთოდები: .islower(), .isupper(), .istitle()
# st = "Morgan Adams"

# print(st.islower())
# print(st.isupper())
# print(st.istitle())




# მეთოდები .strip(), .lstrip(), rstrip()
# text = '     Python is programming language     '
# print(text)
# print("'" + text.upper() + "'", "\n")

# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())



# # მეთოდი .split()
# text = '     Python is programming language     '
# print(text.split(), "\n")
# print(text.split(' '))



# # მეთოდი .join()

# # სრიქონების სია გარდავქმნათ ერთიან სტრიქონად.

# # ["Paata", "Teona", "Demetre", "Alexandre"]   =====> list
# # Users: Paata, Teona, Demetre, Alexandre      =====> str

# users = ["Paata", "Teona", "Demetre", "Alexandre"]
# print(users, type(users), "\n")

# context = "Users: " + ', '.join(users)
# print(context, type(context))



# ოპერატორი in

# შევამოწმოთ არის თუ არა სიმბოლო ან ქვესტრიქონი სტრიქონში

# st = "My first commit"
# ch = 'g'

# print(ch in st)
# print('st comm' in st)
# print('first' in st)
# print('First' in st)



# st = "სტრიქონი"
# print(st * 15, "\n")

# st = "სტრიქონი "
# print(st * 15, "\n")

# st = "სტრიქონი\n"
# print(st * 5)




# f`-სტრიქონი – f-string
# first_name = input("First neme: ")
# last_name = input("last neme: ")
# profession = "Programmer, Poligraf designer"
# country = "Georgia"
# city = "Tbilisi"

# print("\nWelcome", first_name, last_name, ". I am from", country, ". The capital of Georgia is", city, ".")
# print("\nWelcome " + first_name + " " + last_name + ". I am from " + country + ". The capital of Georgia is " + city + ".")
# print(f"\nWelcome {first_name} {last_name}. I am from {country}. The capital of georgia is {city}.")



# num1 = 10
# num2 = 20

# print(f"{num1} + {num2} = {num1 + num2}")
# print(f"{num1} - {num2} = {num1 - num2}")
# print(f"{num1} * {num2} = {num1 * num2}")
# print(f"{num1} / {num2} = {num1 / num2}")
# print(f"{num1} // {num2} = {num1 // num2}")
# print(f"{num1} % {num2} = {num1 % num2}")




# რიცხვითი მონაცემების ფორმატირება
# x = 12.345678

# print(f"{x:.2f}")
# print(f"{x:.3f}")
# print(f"{x:.4f}\n")

# x = 0.85
# print(f"{x:.1%}")
# print(f"{x:.2%}")
# print(f"{x:.3%}")
# print(f"{1.85:.2%}\n")

# x = 10 ** 9
# print(f"{x:,}")



# # Regular Expressions Regex

# import re

# text = "My contacts is 555-123-4567"

# pattern = r"\d{3}-\d{3}-\d{4}"

# match = re.search(pattern, text)

# print(match.group(0))




# # ჯგუფებიანი Regex-ის პრაქტიკული მაგალითი

# # ვთქვათ, გვინდა ტელეფონის ნომრის ნაწილებად მიღება:

# import re

# text = "555-123-4567"

# pattern = r"(\d{3})-(\d{3})-(\d{4})"

# match = re.search(pattern, text)

# area_code = match.group(1)
# prefix = match.group(2)
# line_number = match.group(3)

# print(area_code)
# print(prefix)
# print(line_number)





# # სახელებიანი ჯგუფები

# # უფრო პროფესიონალური ვარიანტია:

# import re

# text = "555-123-4567"

# pattern = r"(?P<code>\d{3})-(?P<prefix>\d{3})-(?P<number>\d{4})"

# match = re.search(pattern, text)

# print(match.group("code"))
# print(match.group("prefix"))
# print(match.group("number"))

# # აქ უკვე group(1)-ის დამახსოვრება აღარ გვჭირდება, რადგან სახელებით მივმართავთ.





# import re

# phone = input("შეიყვანე ტელეფონის ნომერი: ")

# pattern = r"^\d{3}-\d{3}-\d{4}$"

# if re.match(pattern, phone):
#   print("ტელეფონის ნომერი სწორია")
# else:
#   print("ტელეფონის ნომერი არასწორია")





# ქვეყნის კოდი +995 დავამატოთ

# import re

# phone = input("შეიყვანე ტელეფონის ნომერი (+995 555 25 89 00): ")

# pattern = r"^\+\d{3} \d{3} \d{2} \d{2} \d{2}$"
# pattern = r"^\+\d{3}\s\d{3}\s\d{2}\s\d{2}\s\d{2}$"

# print(re.match(pattern, phone).group())



import re

phone = input("შეიყვანე ტელეფონის ნომერი ((+995) 555 25 89 00): ")

pattern = r"^\(\+\d{3}\) \d{3} \d{2} \d{2} \d{2}$"
pattern = r"^\(\+\d{3}\)\s\d{3}\s\d{2}\s\d{2}\s\d{2}$"

print(re.match(pattern, phone).group())