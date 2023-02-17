def fiveGO():
    sqr = 0
    count = 20
    continue_1 = True
    total_1s = input('How many ones do you have?\n')
    total_2s = input('How many twos do you have?\n')
    total_3s = input('How many threes do you have?\n')
    total_4s = input('How many fours do you have?\n')
    total_5s = input('How many fives do you have?\n')
    total_6s = input('How many sixes do you have?\n')
    total_7s = input('How many sevens do you have?\n')
    total_8s = input('How many eights do you have?\n')
    total_9s = input('How many nines do you have?\n')
    total_10s = input('How many tens do you have?\n')
    total_list = [total_1s, total_2s, total_3s, total_4s, total_5s, total_6s, total_7s, total_8s, total_9s, total_10s]
    for string in total_list:
        if string.isdigit() == False:
            print('One of the numbers that you have inputted is invalid. Please try again.')
            return

    for number in total_list:
        if count > 0:
            count -= 1
            total_list.remove(number)
            new_number = int(number)
            total_list.insert(0, new_number)
    total_numbers = 0
    for number_0 in total_list:
        total_numbers += number_0
    if total_numbers > 25 or total_numbers < 25:
        print("The numbers you used are not viable for 5x5_GO. Please try again.")
        return
    print('You got past the bug fixes! Now you need to wait for the full version.')
    for number in total_list:
        if number == 0:
            count_0 = number
            total_list.remove(number)
            number_shape = 'Null{number}'
            total_list.insert(0, number_shape)
        elif number == 1:
            count_0 = number
            total_list.remove(number)
            number_shape = 'Filler{number}'
            total_list.insert(0, number_shape)
        elif number == 2:
            count_0 = number
            total_list.remove(number)
            number_shape = 'Line{number}'
            total_list.insert(0, number_shape)
        elif number == 3:
            count_0 = number
            total_list.remove(number)
            number_shape = 'L{number}'
            total_list.insert(0, number_shape)
        elif number == 4:
            count_0 = number
            total_list.remove(number)
            number_shape = 'Square{number}'
            total_list.insert(0, number_shape)
            sqr = sqr + 1
            if sqr >= 5:
                total_list.remove(number_shape)
                total_list.insert(0, 'longL{number}')
    print(total_list)
    input("")
fiveGO()
# just use 3, 3, 3, 3, 3, 2, 2, 2, 2, 2