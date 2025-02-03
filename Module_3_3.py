def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [15, 'pedik', False]
values_dict = {'a' : 52,'b' : 'pizdec', 'c' : 52.35}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['yo!', 52]
print_params(*values_list_2, 42)