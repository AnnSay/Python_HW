my_int = 25
my_float = 2.5
my_str = "Hello world"
my_list = ['a', '2']
my_tuple = ('b', '3')
my_set = {400, None, "text", True}
my_dict = {'city': 'Moscow', 'country': 'Russia'}
my_bool = 3>2

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_set, my_dict, my_bool]
for i in super_list:
    print(f'{i} is {type(i)}')