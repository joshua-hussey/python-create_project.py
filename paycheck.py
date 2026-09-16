# Name: Joshua Hussey
# Date: 09-15-2026
# Course: COMP 163
# Project 1: Paycheck Calculator

# Put your name after "# Name:" above. The grader checks that it is filled in.

employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: ))
tax_rate = float(input("Enter tax rate as a percent: "))

gross_pay = hours_worked * hourly_rate
tax_withheld = gross_pay * (tax_rate/100)
net_pay = gross_pay - tax_withheld

# Then print the four required output lines.
# The exact format is in README.md. Match it exactly or the tests will fail.
#
# Chapters 1 and 2 only. Use variables, input(), arithmetic, type conversion,
# and print(). Do not use if statements, loops, functions, or imports.
# Your code runs top to bottom, once.
