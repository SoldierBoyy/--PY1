import random
import string

def get_random_password(password_size) -> str:
    alphabet_ = string.ascii_uppercase + string.ascii_lowercase + string.digits
    n = random.randrange(password_size, len(alphabet_), 1)
    password = "".join(random.sample(alphabet_, n))
    return password
    # TODO написать функцию генерации случайных паролей
result_password = get_random_password(8)

print(result_password)