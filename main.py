from email_validator import validate_email, EmailNotValidError
import re
import is_disposable_email

def valide_or_not(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pattern, email):
        print("This is an VALID Email Address")
    else:
        print("This is an INVALID Email Address")

def deliverable_or_not(email):
    try:
        emailinfo = validate_email(email, check_deliverability=True)
        email = emailinfo.normalized
        print("This Email is DELIVERABLE")
    except EmailNotValidError as e:
        print("This Email is NOT DELIVERABLE")
        print(str(e))

def disposable_or_not(email):
    result = is_disposable_email.check(email)
    if (result == True):
        print("This Email is DISPOSABLE")
    else:
        print("This is NON DISPOSABLE Email")

email = input("Enter the email address:")

valide_or_not(email)
deliverable_or_not(email)
disposable_or_not(email)







