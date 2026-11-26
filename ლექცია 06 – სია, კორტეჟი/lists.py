# # ცარიელი სია

# empty_lst = []
# print(empty_lst)
# print(type(empty_lst), "\n")

# empty_lst = list()
# print(empty_lst)
# print(type(empty_lst), "\n")



# numbers = [1, 2, 3, 4, 5]
# print(numbers, "\n")

# names = ["John", "Ann", "Bob", "Allice"]
# print(names, "\n")

# mixed_lst = [1, "Python", 3.14, True, 20, False]
# print(mixed_lst, "\n")




# my_list = [1, "str", [5, 8], 2.56, True]

# print(my_list, type(my_list), id(my_list), "\n")

# print(my_list[0], type(my_list[0]), id(my_list[0]))
# print(my_list[1], type(my_list[1]), id(my_list[1]))
# print(my_list[2], type(my_list[2]), id(my_list[2]))
# print(my_list[-1], type(my_list[-1]), id(my_list[-1]), "\n")

# # print(my_list[10])    # IndexError: list index out of range

# print(my_list[2][0], type(my_list[2][0]), id(my_list[2][0]), "\n")





# # ჭრები სიაში – List slicing

# lst = [12, 8, 45, 109, 23, 61, 4, 11, 7, 69, 18]

# print(lst[0:5])
# print(lst[:5])
# print(lst[5:])
# print(lst[3:8])
# print(lst[::2])
# print(lst[::-1])
# print(lst[::-3])
# print(lst[-2:3:-1])




# # სტრიქონები წარმოადგენენ უცლელ მონაცემთა ტიპებს

# name = "Python"
# print(name, id(name)) 

# name = name.lower()
# print(name, id(name)) 



# რადიკალურად განსხვავებული სიტუაცია გვაქვს სიების შემთხვევაში

numbers = [15, 21, 14, 87, 16, 2, 37]
print(numbers, id(numbers))

numbers.append(10)
print(numbers, id(numbers))