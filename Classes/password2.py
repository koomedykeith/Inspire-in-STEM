import string
import secrets
alphabet = string.ascii_letters + string.digits + '-_'
password = ''.join(secrets.choice(alphabet) for i in range(20))
print(password)