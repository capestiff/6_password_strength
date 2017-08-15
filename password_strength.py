import re
from getpass import getpass

# from https://github.com/danielmiessler/SecLists/blob/master/Passwords/500-worst-passwords.txt
PASSWORD_BLACKLIST_PATH = '500-worst-passwords.txt'


def get_eval_score_for_chars(password):
    eval_score = 0
    eval_dict = {
        'lowercase': '[a-z]',
        'uppercase': '[A-Z]',
        'digits': '[0-9]',
        'special_chars': '[ !"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]'
    }
    for key in eval_dict:
        if re.search(eval_dict[key], password):
            eval_score += 1

    return eval_score


def get_eval_score_for_length(password):
    eval_score = 0
    if len(password) in range(8, 16):
        eval_score += 3
    elif len(password) > 16:
        eval_score += 4

    return eval_score


def get_eval_score_for_blacklist(password):
    eval_score = 0
    password_blacklist = get_password_blacklist()
    password_has_blacklist_word = []

    for word in password_blacklist:
        if word in password.lower():
            password_has_blacklist_word.append(word)

    if password not in password_blacklist and not password_has_blacklist_word and len(password) >= 4:
        eval_score += 1

    return eval_score


def get_password_blacklist():
    with open(PASSWORD_BLACKLIST_PATH, 'r') as file:
        password_blacklist = [line.strip() for line in file]

    return password_blacklist


def get_password_strength(password):
    common_eval_score = get_eval_score_for_chars(password) \
                        + get_eval_score_for_length(password) \
                        + get_eval_score_for_blacklist(password)

    return common_eval_score


if __name__ == '__main__':
    user_password = ''
    while not user_password:
        user_password = getpass('Enter your password: ')
    print('Your password has score: {} of 10'.format(get_password_strength(user_password)))
