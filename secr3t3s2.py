import string
import secrets
#GENERATE ALPHANUMERIC 8 CHARACTER PASSWORD#
alphabet = string.ascii_letters + string.digits
password = "".join(secrets.choice(alphabet)for i in range(8))
print(password)

