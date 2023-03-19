# My name: Ana Trias-Labellarte

def menu():
    print('Menu')
    print('------------- ')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


def encode(password):
    new_pass = ''
    for num in password:
        if int(num) >= 7:
            new_pass += str(int(num) - 7)
        else:
            new_pass += str(int(num) + 3)
    return new_pass


while True:
    menu()
    option = int(input('Please enter an option: '))
    if option == 1:
        password = input('Please enter your password to encode: ')
        new_pass = encode(password)
        print('Your password has been encoded and stored!\n')
    if option == 2:
        print(f'The encoded password is {new_pass}, and the original password is {password}.\n')
    if option == 3:
        break
