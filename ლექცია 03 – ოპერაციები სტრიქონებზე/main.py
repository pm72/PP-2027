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



# მეთოდი .replace()
# st = "1 2 3 4 5 6 7 8 9 0"
# print(st.replace('5', 'five'))

# st = "1 2 3 4 5 6 7 8 9 0 5 5 4 8"
# print(st.replace('5', 'five', 2), "\n")


# სტრიქონის სიგრძე (სმბოლოების რაოდენობა) – ფუნქცია len()
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
first_name = input("First neme: ")
last_name = input("last neme: ")
profession = "Programmer, Poligraf designer"
country = "Georgia"
city = "Tbilisi"

print("\nWelcome", first_name, last_name, ". I am from", country, ". The capital of Georgia is", city, ".")
print("\nWelcome " + first_name + " " + last_name + ". I am from " + country + ". The capital of Georgia is " + city + ".")
print(f"\nWelcome {first_name} {last_name}. I am from {country}. The capital of georgia is {city}.")