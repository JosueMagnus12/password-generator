import secrets
upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
special_characters = ['*','+','#','@','_','-','&','%','$','!','/','?']
characters = upper_case + lower_case + numbers + special_characters


def generate_password(n):
    password = ""
    for i in range(n):
        password += secrets.choice(characters)
    return password

if __name__ == "__main__":
    num = int(input("How many characters long?: "))
    password = generate_password(num)
    print("Your password is: " + password)