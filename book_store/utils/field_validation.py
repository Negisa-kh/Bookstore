

def is_number(number):
    if len(number) == 11 and number[0:2] == "09":
        return True
    return False




def check_password(password):
    if len(password) < 8:
        return False
    