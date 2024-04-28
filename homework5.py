my_list =['apple', 'lemon', 'strawberry', 'watermelon', 'peach']
print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[2:])
my_list[2]='orange'
print(my_list)

my_dict = {'apple':'яблоко', 'lemon': 'лимон', 'strawberry': 'клубника', 'watermelon': 'арбуз', 'peach': 'персик'}
print(my_dict)
print(my_dict.get('apple'))
my_dict['apple'] = 'груша'
my_dict['orange'] = 'апельсин'
print(my_dict)