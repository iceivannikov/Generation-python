DOMAIN = "@beegeek.bzz"

def corporate_mail(emails, name):
    email = name + DOMAIN
    if email not in emails:
        emails.add(email)
        return email

    number = 1
    while True:
        email = name + str(number) + DOMAIN
        if email not in emails:
            emails.add(email)
            return email
        number += 1



if __name__ == "__main__":
    n = int(input())
    emails = {input() for _ in range(n)}
    m = int(input())
    for _ in range(m):
        name = input()
        print(corporate_mail(emails, name))


"""
6
ivan-petrov@beegeek.bzz
petr-ivanov@beegeek.bzz
ivan-petrov1@beegeek.bzz
ivan-ivanov@beegeek.bzz
ivan-ivanov1@beegeek.bzz
ivan-ivanov2@beegeek.bzz
3
ivan-ivanov
petr-petrov
petr-ivanov
"""