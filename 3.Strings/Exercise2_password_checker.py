user_name=input("User name = ")
password=input("Password = ")

password_len=len(password)
secret_password = password_len*'*'

print(f"{user_name}, your password {'*'*password_len} is {password_len} letters long")
print("%s, your password %s is %d letters long" % (user_name, secret_password, password_len))
print("{0}, your password {1} is {2} letters long".format(user_name, secret_password, password_len))
