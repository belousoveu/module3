def validate_email(email_address, regex=('.com', '.org', '.ru', '.net')):
    if '@' in email_address and email_address.endswith(regex):
        return True
    else:
        return False


def send_email(message, recipient, *, sender=None):
    ''' Пояснение. Можно конечно было значение по умолчанию сразу записать в строке определения функции.
    Но в этом случае я не нашел, как можно в Python проверить был ли изменен параметр по умолчанию. У нас по условию
    далее выполняется проверка на "нестандартного отправителя" и в таком случае нам бы пришлось сравнивать параметр
      sender с литералом. Это не очень хорошо, поскольку в последующем может привести в ошибке. Если в какой-то момент
      времени нам потребуется поменять стандартный адрес отправителя - то нужно будет менять все литералы. Правильнее
      значение по умолчанию, присвоить переменной sender_default и дальнейшие сравнения производить с ней
    '''

    sender_default = 'university.help@gmail.com'
    if sender is None:
        sender = sender_default
    if not validate_email(recipient):
        return (f'Адрес получателя {recipient} указан некорректно\n'
                f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if not validate_email(sender):
        return (f'Адрес отправителя {sender} указан некорректно\n'
                f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if recipient == sender:
        return (f'Адреса отправителя {sender} и получателя {recipient} совпадают \n'
                f'Вы не можете отправлять сообщения самому себе')
    if sender != sender_default:
        return f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! \nПисьмо отправлено с адреса {sender} на адрес {recipient}'
    return f'Письмо отправлено с адреса {sender} на адрес {recipient}'


print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(
    send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))
