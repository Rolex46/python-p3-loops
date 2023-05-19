#!/usr/bin/env python3

def happy_new_year():
    i = 10
    
    while i > 0:
        print(i)
        i -= 1
    
    print("Happy New Year!")

def square_integers(int_list):
    squared_list = []
    
    for n in int_list:
        squared_list.append(n ** 2)
    
    return squared_list 
    

def fizzbuzz():
    for n in range(1,101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)
    
