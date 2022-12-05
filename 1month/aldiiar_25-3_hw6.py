# 1
def first_w(string):
    if type(string) != str:
        return False
    else:
        return string.split()[0]

print(first_w(6578))



# 2
def average(*integer):

    return sum(integer) / len(integer)

print(int(average(2, 3, 5, 5, 6)))



# 3
def reliability(password):
    if len(password) >= 6 and not password.isdigit() and not password.isalpha():
        return True
    else:
        return False

print(reliability('87687'))






