# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:04:33 2024

@author: User
"""

# Textbook Reading: read chapter 5, 7
# A. write N factorial using 1) while loop  2) for loop
# B. calculate weekly wage, given hourly wage and hours worked. Overtime (hours worked above 40) pay is 1.5 times regular wage.
# C. Ask the user to enter a month number between 1 and 12. The following seasons are associated with these months:
# Winter: 12, 1, 2   Spring: 3, 4, 5  Summer: 6, 7, 8  Fall: 9, 10, 11
# Example:
#      Enter a month number: 10
#      It is Fall
#      Also: Check for legal input (valid entries are 1-12). If not a legal number output:  "Invalid month. Enter number 1-12"

# D. Project Proposal due in one week
# What to turn in : 
# Code and output
# Code comment section explains program and also your name & date etc
def factorial_while_loop():
    while True:
        N=int(input('Please input N to do N factorial in While loop: '))
        result = 1
        if N == 0:
            print(f'Factorial of {N} is:', 1)
        else:
            while N >1:
                result*=N
                N-=1
            print(f'Factorial of {N} is:', result)
        to_continue = input('do you want to continue? (Y/N)').lower()  
        if to_continue !='y':
            break
factorial_while_loop()

    
def factorial_for_loop():
    while True:
        N=int(input('Please input N to do N factorial in For loop: '))
        result =1
        for n in range (1, N+1):
            result*=n
        print(f'Factorial of {N} is:', result) 
        to_continue = input('Do you want to continue? (Y/N): ').strip().lower()
        if to_continue != 'y':
            break
factorial_for_loop()
    

def weekly_wage():
    while True:
        while True:
            try:
                hourly_wage= float(input('please input your hourly wage ($): '))
                break
            except ValueError:
                print('Please input a valid number for hourly wage!')            
        while True:
            try:
                weekly_working_hours = int(input('please input your total weekly working hours: '))
                if weekly_working_hours > 40:
                        overtime_hours = weekly_working_hours-40
                        weekly_wage = hourly_wage*(40 + overtime_hours*1.5)
                        print(f'user worked {overtime_hours} overtime, so weekly wage is: ', weekly_wage)
                else: 
                        weekly_wage = hourly_wage*weekly_working_hours
                        print("user's weekly wage ($): ", weekly_wage)
                break
            except ValueError:
                    print('Please input a valid number for working hours!')
        to_continue = input('Do you want to continue? (Y/N): ').strip().lower()
        if to_continue != 'y':
            break
weekly_wage()


def season():
    while True:
        month = input( 'Enter a month number (1-12): ')
        if month.isdigit() and int(month) in range(1,13):
            month=int(month)
            if month in [12,1,2]:
                print ('It is Winter')
            elif month in [3,4,5]:
                print ('It is Spring')
            elif month in [6,7,8]:
                print ('It is Sumer')
            else:
                print ('It is Fall')
            to_continue = input('Do you want to continue? (Y/N): ').lower()
            if to_continue != 'y':
                break
        else: print('Invalid month. Enter number 1-12')
season() 

        
        
    