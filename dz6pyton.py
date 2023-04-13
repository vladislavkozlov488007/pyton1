while True:
    number = input('Введите шестизначный номер Вашего билета: ')
    if number.isdigit() and len(number) == 6:
        if sum(map(int, number[:3])) == sum(map(int, number[3:])):
            print('счастливый!')
        else:
            print(' не счастливый(')
        break
    else:
        print('Введен некорректный номер билета, попробуйте еще раз)')