def collatz(number):
    if number % 2 == 0:
        number_even_return = number // 2
        print(number_even_return)
        return number_even_return
    elif number % 2 == 1:
        number_odd_return = number * 3 + 1
        print(number_odd_return)
        return number_odd_return



while True:
    user_input = input("Enter number: ")
    try:
        number = int(user_input)
        break
    except ValueError:
        print("Enter an integer.")
        continue

while number != 1:
    number = collatz(number)
