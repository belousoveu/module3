calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(s):
    count_calls()
    return len(s), s.upper(), s.lower()


def is_contains(s, list_):
    count_calls()
    return s.lower() in [str_.lower() for str_ in list_]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Python'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('.PY', ['.EXE', '.com', '.bat', '.py']))
print(calls)
