immutable_var = (1, 2, 3, True, 'pisyat dva')
print(immutable_var)
# immutable_var[2] = 52 -> кортеж является неизменяемым типом данных
mutable_list = [1, 2, 3, False, 'pisyat dva']
print(mutable_list)
mutable_list[0]=52
mutable_list[1]=52
mutable_list[2]=52
mutable_list[3]=True
print(mutable_list)