secret_word = 'test'
correct_letters = ''
attempts = 0

while True:
    user_choice = str(input('Escolha uma letra: ')).lower()
    attempts += 1

    if len(user_choice) > 1 or len(user_choice) < 1 or not user_choice.isalpha():
        print('Você precisa digitar uma letra')
        continue

    
    if user_choice in secret_word:
        correct_letters += user_choice

    formed_word = ''
    for i in secret_word:
        if i in correct_letters:
            formed_word += i
        else:
            formed_word += '*'

    print(formed_word)

    if formed_word == secret_word:
        print(f'Parabéns! Você venceu em {attempts} tentativas.')
        break