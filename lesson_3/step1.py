def my_func(num1, num2):
    try:
        result = num1 / num2
        print(int(result))
    except ZeroDivisionError or ValueError:
        print("error")

my_func(9, 3)
