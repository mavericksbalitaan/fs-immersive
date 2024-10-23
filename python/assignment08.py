'''
Part 1:

Write a program that calculates the result using the following formula:

result=3x+5y

'''

def calculate_result():
    x = int(input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))
    result = 3*x + 5*y
    print(f"The result is {result}")

calculate_result()

'''

Part 2:
    Pay calculator

    This program should calculate the pay of an employee based on hours worked. The input includes the employee’s total hours worked per week and their hourly pay rate. The employee will be paid a base wage for the first 40 hours worked and time-and-a-half (150% of base pay) for any hours past 40 as overtime pay. Output the regular pay, overtime pay, and total pay for the week on the screen.

If the employee worked 40 hours or less, don’t show any output regarding overtime pay.

'''

def pay_calculator():
    hours = int(input("Enter the total hours worked per week: "))
    rate = float(input("Enter the hourly pay rate: "))
    if hours <= 40:
        regular_pay = hours * rate
        print(f"Regular pay: ${regular_pay}")
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * rate * 1.5
        total_pay = regular_pay + overtime_pay
        print(f"Regular pay: ${regular_pay}")
        print(f"Overtime pay: ${overtime_pay}")
        print(f"Total pay: ${total_pay}")

pay_calculator()
