import requests

eng_morse_coder = requests.get('https://api.npoint.io/cd6ef34305c8c36f90aa').json()


def encoder(message):
    output = ''
    for letter in message.upper():
        if letter != ' ':
            output += eng_morse_coder[letter] + ' '
        else:
            output += '/ '
    return output


def decoder(message):
    output = ''
    morse_letters = message.split()
    for letter in morse_letters:
        if letter != '/':
            for key, value in eng_morse_coder.items():
                if letter == value:
                    output += key
        else:
            output += ' '

    return output


language = input('What language you want to use in morse coder/decoder?').lower()

while True:
    operation = input('What do you want to do with message? (E/D) ')
    if language == 'eng':
        if operation == 'E':
            print(encoder(input('Enter your message: ').upper()))
            if input('Wanna code another message? ') == 'Yes':
                continue
            else:
                break
        elif operation == 'D':
            print(decoder(input('Enter your message: ').upper()))
            if input('Wanna code another message? ') == 'Yes':
                continue
            else:
                break
        elif operation == 'Q':
            break
        else:
            print('If u want to quit, just type "Q"')
            continue
    else:
        print('We have no this language in DataBase, please, enter another message')
        break
