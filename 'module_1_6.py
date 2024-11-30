my_dict = {'Pavel': 2002, 'Ivan': 2003, 'Max': 2004}
print(my_dict)
print(my_dict.get('Ivan'))
print(my_dict.get('Egor'))
my_dict.update({'Alex': 1999,
                'Kolya': 2000})
print(my_dict)
print(my_dict.pop('Pavel'))
print(my_dict)

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 4, 7, 8}
print(my_set)
my_set.add(52)
my_set.add(48)
print(my_set)
my_set.discard(1)
print(my_set)