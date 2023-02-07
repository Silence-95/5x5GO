count = 20
continue_1 = True
total_1s = input('how many ones do you have?')
total_2s = input('how many ones do you have?')
total_3s = input('how many ones do you have?')
total_4s = input('how many ones do you have?')
total_5s = input('how many ones do you have?')
total_6s = input('how many ones do you have?')
total_7s = input('how many ones do you have?')
total_8s = input('how many ones do you have?')
total_9s = input('how many ones do you have?')
total_10s = input('how many ones do you have?')
total_list = [total_1s, total_2s, total_3s, total_4s, total_5s, total_6s, total_7s, total_8s, total_9s, total_10s]
for string in total_list:
    if string.isdigit() == True:
        print('good')
    else:
        print('why')
        continue_1 = False
if continue_1 == True:
    for number in total_list:
        if count > 0:
            count -= 1
            total_list.remove(number)
            new_number = int(number)
            total_list.append(new_number)
print(total_list)