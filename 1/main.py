"""
Задание: Напишите программу, где пользователь вводит любое целое положительное число.
А программа суммирует все числа от 1 до введенного пользователем числа.
В качестве выполненного ДЗ отправить файл с расширением .py
"""
i = 1
result = 0

while True:
    user_number = input("Введите число: ")
    if user_number.isdigit():
        user_number = int(user_number)
        break
    else:
        print("Нужно вводить число")
        continue

for i in range(i, user_number+1):
    result += i
    i += 1

print(result)
