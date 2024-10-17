#Elias (EJ) Quintos

def encode():
    res = ''
    isnumeric = False
    while not isnumeric:
        strPassword = input("Please enter your password to encode: ")
        if strPassword.isnumeric():
            isnumeric = True
    for i in strPassword:
        temp = int(i) + 3
        res = res + str(temp)[-1]
    return res


if __name__ == '__main__':
    running = True
    password = None
    while running:
        print('''Menu
-------------
1. Encode
2. Decode
3. Quit\n''')
        userOption = int(input("Please enter an option: "))
        if userOption == 1:
            password = encode()
            print("Your password has been encoded and stored!\n")
        elif userOption == 2:
            if not password:
                print("Nothin has been encoded yet.\n")
            else:
                print(f'The encoded password is {password}, and the original password is {decode(password)}')
        else:
            running = False