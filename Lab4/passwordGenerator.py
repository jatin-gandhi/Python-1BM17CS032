import string
import random
passw= string.ascii_letters + string.digits+string.punctuation  
password = "".join(random.choices(passw,k=8))
print(password)
