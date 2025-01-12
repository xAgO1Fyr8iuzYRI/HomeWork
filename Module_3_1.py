calls = 0

def count_calls():
    global calls
    calls = calls + 1
    return calls

def string_info(string):
    count_calls()
    info = (int(len(string)), string.upper(), string.lower())
    return info

def is_contains(string, list_to_search):
    count_calls()
    string = string.upper()
    for i in range(int(len(list_to_search))):
        list_to_search[i] = list_to_search[i].upper()
    if string not in list_to_search:
        return False
    else:
        return True



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('cool', ['clool', 'CoaL', 'CooL']))
print(calls)