import random
import string

def random_user_id(number):
    random_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(number)])
    
    return random_id

print(random_user_id(6))
