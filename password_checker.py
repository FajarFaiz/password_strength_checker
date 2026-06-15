
#password strength checker

import re

#password strength checker conditions:
#min 8 characters,digit,uppercase,lowercase & special characters
def check_password_strength(password):
    if len(password) < 8: # length of password
        return "Weak: password must be at least 8 characters"
    
    if not any(char.isdigit() for char in password):
        return "Weak: password must contain at least one digit"
    
    if not any(char.isupper() for char in password):
        return "Weak: password must contain at least one uppercase letter"
    
    if not any(char.islower() for char in password):
        return "Weak: password must contain at least one lowercase letter"
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        return "Weak: password must contain at least one special character"
    
    return "Strong: password is strong!"

def password_checker():

    while True:
        password = input("Enter your password (or type 'exit' to quit): ") 

        if password.lower() == "exit":
            print("Exiting password checker.")
            break
        result = check_password_strength(password)
        print(result)

# Run the password checker tool
if __name__ == "__main__": 
    password_checker()

  
    
    
    