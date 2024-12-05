first_number = int(input('Type your number(3-20): '))
while first_number < 3 or first_number > 20:
    first_number = int(input('Wrong number, try again: '))

def find_password(key):
    list_ = []
    for i in range(1,21):
        for j in range(1,21):
            if key % (i + j)  == 0 and i + j <= key and i != j:
                list_.append([i, j])
            if j >= key:
                break
        if i >= key:
            break
    return list_

unsorted_password = find_password(first_number)

def find_unique_pairs(pairs):
    unique_pairs = set()
    result = []
    for pair in pairs:
        sorted_pair = tuple(sorted(pair))
        if sorted_pair not in unique_pairs:
            unique_pairs.add(sorted_pair)
            result.append(pair)
    return result

password_list = find_unique_pairs(unsorted_password)

def make_good_password(listok):
    good_password = ''
    for i in range(int(len(listok))):
        for j in range(2):
            good_password = good_password + str(listok[i][j])
    return good_password

password = make_good_password(password_list)
print(f'Your password is: {password}')
