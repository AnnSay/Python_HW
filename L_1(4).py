user_number = abs(int(input("Введите целое число: ")))
max_number=0
while user_number > 0:
    item = user_number%10
    if item>=max_number:
        max_number=item

    user_number = user_number // 10

print(max_number)