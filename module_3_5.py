def get_multiplied_digits_list(number):  # Решаем через список
    list_of_digits = list(str(number))
    if len(list_of_digits) != 1:  # если осталось больше одной цифры - уходим в рекурсию, иначе возвращаем эту цифру
        return int(list_of_digits.pop()) * get_multiplied_digits_list(int("".join(list_of_digits)))
    else:
        return int(list_of_digits.pop())


def get_multiplied_digits_str(number):  # Решаем через строку
    string_of_digits = str(number)
    if len(string_of_digits) != 1:  # если осталось больше одной цифры - уходим в рекурсию, иначе возвращаем эту цифру
        return int(string_of_digits[0]) * get_multiplied_digits_str(int(string_of_digits[1:]))
    else:
        return int(string_of_digits[0])


print(get_multiplied_digits_list(61235))

print(get_multiplied_digits_str(61235))
