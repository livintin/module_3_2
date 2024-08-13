def send_email(message, recipient, sender="university.help@gmail.com"):
    # Проверка на совпадение
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    # Проверка на @
    if "@" not in sender or "@" not in recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    # Проверка почты на end = ['.com', '.ru', '.net']
    end = ['.com', '.ru', '.net']
    true_end_sender = False
    for i in end:
        if sender.endswith(i):
            true_end_sender = True
            break
    if not true_end_sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    true_end_recipient = False
    for i in end:
        if recipient.endswith(i):
            true_end_recipient = True
            break
    if not true_end_recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    # Проверка отправителя
    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
