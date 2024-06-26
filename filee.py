import simplecrypt
import urllib.request as urllib

passwords = urllib.urlopen('https://stepik.org/media/attachments/lesson/24466/passwords.txt')

encrypted = urllib.urlopen('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').read()

for password in passwords:
    password = password[:-1]
    try:
        print(simplecrypt.decrypt(password, encrypted).decode('utf8'))
    except simplecrypt.DecryptionException:
        print(password, 'is wrong')
    else:
        print(password, 'is correct')

