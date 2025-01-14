# password strength checker

import re

# password strength checker conditions:
# min 8 char , digit, uppercase, lowercase & special characters

def check_password_strength(password):
    if len(password) < 8 :      #length of the password
        return "password must be atleast 8 char"
    
    if not any(char.isdigit() for char in password):
        return "weak : password must contain a digit"
    
    if not any(char.isupper() for char in password ):     # check uppercase in password
        return "weak : password must contain uppercase"
    
    if not any(char.islower() for char in password ):     # check lowercase in password
        return "weak : password must contain lowercase"
 
    if not re.search(r'[!@#$%^&*(){}:<>?]', password):     # check special char
        return "password must contain a special char"
    
    return "Strong : your password is secured! "


def password_checker():
    print ("Welcome to the password strength checker")

    while True:
        password = input("Enter your password (or type 'exit' to quit):")

        if password.lower() == 'exit':
            print("Thank you for using this tool")
            break

        result = check_password_strength(password)      #passing this as an arguement for the while loop.
        print(result)


# run the password checker 
if __name__ == "___main__":
    password_checker()
