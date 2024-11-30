first = int(input('Type your first number:'))
second = int(input('Type your second number:'))
third = int(input('Type your third number:'))
if first==second==third:
    print('3')
elif first==second!=third or second==third!=first or first==third!=second:
    print('2')
else:
    print('0')