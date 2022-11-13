import random
import string

def get_random_password() -> str:
    alphabet_ = string.ascii_uppercase + string.ascii_lowercase + string.digits
    n = random.randrange(8, len(alphabet_), 1)
    password = "".join(random.sample(alphabet_, n))
    return password
  # TODO написать функцию генерации случайных паролей

print(get_random_password())
