import re


def get_password_blacklist():
    # I've got this password_blacklist from:
    # https://github.com/danielmiessler/SecLists/blob/master/Passwords/500-worst-passwords.txt
    with open('500-worst-passwords.txt', 'r') as file:
        password_blacklist = [line.strip() for line in file]

    return password_blacklist


def get_password_strength(password):
    evaluation_point = 0

    # evaluating for length
    if len(password) in range(8, 16):
        evaluation_point += 1
    elif len(password) > 16:
        evaluation_point += 2

    # evaluating for lowercase
    if re.search('[a-z]', password):
        evaluation_point += 1

    # evaluating for uppercase
    if re.search('[A-Z]', password):
        evaluation_point += 1

    # evaluating for digits
    if re.search('[0-9]', password):
        evaluation_point += 1

    # evaluating for non-alphanumeric symbols
    if re.search('\W+', password):
        evaluation_point += 1

    # evaluating for special characters @, #, $, %
    if re.search('[@#$%]', password):
        evaluation_point += 1

    # evaluating the password isn't in and hasn't words from the blacklist
    password_blacklist = get_password_blacklist()
    password_has_blacklist_word = False

    for word in password_blacklist:
        if word in password.lower():
            password_has_blacklist_word = True

    if password not in password_blacklist and not password_has_blacklist_word:
        evaluation_point += 2

    return evaluation_point


if __name__ == '__main__':
    user_password = ''
    while len(user_password) < 6:
        user_password = input('Enter your password (6 characters or more): ')
    print('Your password has score: {} of 10'.format(get_password_strength(user_password)))
