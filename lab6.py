#Katie Ardoin

def menu_options():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def encode():
    password = input('Please enter your password to encode: ')
    encoded = ''
    for item in password:
        encoded += str(int(item) + 3)
    return encoded
    print('Your password has been encoded and stored!')

def decode(password): #Add Decoder here
    return None

if __name__ == '__main__':
    while True:
        print(menu_options())
        choice = input('Please enter an option: ')
        if choice == '1':
            password = encode()

        if choice == '2':
            decoded = decode(password)
            print('The encoded password is ' + password +', and the original password is ' + decoded + '.')

        if choice == '3':
            exit()

