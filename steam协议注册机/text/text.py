from itertools import cycle
count = 0


def method_name():
    emails = cycle(open('../utils/chehll.txt').read().splitlines())
    while True:
        global count
        try:
            count += 1
            email = next(emails)
            account_mail = email.split(":")[0]
            account_pass = email.split(":")[1]
            print(account_mail)
            print(account_pass)
        except Exception as e:
            print(e)


method_name()

