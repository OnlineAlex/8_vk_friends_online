import vk
from vk.exceptions import VkAuthError
import getpass

APP_ID = 6421078


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session, v=5.73)
    friends_online = api.users.get(
        user_ids=api.friends.getOnline()
    )

    return friends_online


def output_friends_to_console(friends_online):
    print('Друзей онлайн — {}'.format(len(friends_online)))
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    user_login = input('Ваша почта или телефон: ')
    user_password = getpass.getpass(prompt='Ваш пароль:')
    try:
        user_friends_online = get_online_friends(user_login, user_password)
    except VkAuthError:
        exit('Неверный логин или пароль')
    output_friends_to_console(user_friends_online)
