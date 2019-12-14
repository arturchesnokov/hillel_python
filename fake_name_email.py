from faker import Faker


def names_emails(count):
    fake = Faker()
    user_list = ""
    for i in range(count):
        email = fake.email()
        user_list += '<br>' + fake.name() + ': <a href="mailto:' + email + '">' + email + '</a>'
    return user_list


if __name__ == '__main__':
    print(names_emails(5))
