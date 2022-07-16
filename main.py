from api import check_token, create_short_link, send_to_mail


if __name__ == "__main__":
    check_token('')
    create_short_link('https://vk.com/id1')
    send_to_mail('Subject', 'Body', 'mail')
