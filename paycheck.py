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
tax_withheld = gross_pay * (tax_rate / 100)
net_pay = gross_pay - tax_withheld

# Then print the four required output lines.
print(f"Employee: {employee_name}")
print(f"Gross pay: ${gross_pay:.2f}")
print(f"Tax withheld ${tax_withheld:.2f}")
print(f"Net pay ${net_pay:.2f}")
