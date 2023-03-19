import requests

eng_morse_coder = requests.get('https://api.npoint.io/cd6ef34305c8c36f90aa').json()


def encoder(message):
    output = ''
    for letter in message:
        if letter != ' ':
            output += eng_morse_coder[letter]
        else:
            output += ' '
    return output


flag = True
language = input('What language you want to use in morse coder/decoder?').lower()
while flag:
    if language == 'eng':
        print(encoder(input('Enter your message: ').upper()))
        if input('Wanna code another message? ') == 'Yes':
            continue
        else:
            break
    else:
        print('We have no this language in DataBase, please, enter another message')
        break
