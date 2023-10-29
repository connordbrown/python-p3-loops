#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while (num > 0):
        print(num)
        num -= 1
    print('Happy New Year!')

def square_integers(int_list):
    return [element ** 2 for element in int_list]

def fizzbuzz():
    i = 1;
    while (i <= 100):
        if ((i % 3 == 0) and (i % 5 == 0)):
            print("FizzBuzz")
        elif (i % 5 == 0):
            print("Buzz")
        elif (i % 3 == 0):
            print("Fizz")
        else:
            print(i)
        i += 1         
        
