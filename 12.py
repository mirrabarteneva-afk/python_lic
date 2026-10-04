import secrets
from string import digits, ascii_letters


def gen_pwd(length=8):
    chars = digits + ascii_letters
    return ' '.join(secrets.choice(chars) for c in range(length))

def gen_s_pwd(length=16, upper=3, digits=3):
    if length < upper + digits + 1:
        raise ValueError('Nice try!')
    while True:
        pwd = gen_pwd(length)
        if (
            any(c.islower() for c in pwd)
            and sum(c.isupper() for c in pwd) >= upper
            and sum(c.isdigit() for c in pwd) >= digits
        ):
            return pwd
        
print(gen_s_pwd())
print(gen_s_pwd(length=3, upper=1, digits=1))