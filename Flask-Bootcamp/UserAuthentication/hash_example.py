from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'supersecretpassword'

hashed_pwd = bcrypt.generate_password_hash(password=password)

print(hashed_pwd)
check = bcrypt.check_password_hash(hashed_pwd, 'wrongpassword')
print(check)

check = bcrypt.check_password_hash(hashed_pwd, 'supersecretpassword')
print(check)


from werkzeug.security import generate_password_hash, check_password_hash

hashed_pass = generate_password_hash('mypassword')
print(hashed_pwd)
check = check_password_hash(hashed_pass, 'wrong')
print(check)
check = check_password_hash(hashed_pass, 'mypassword')
print(check)
