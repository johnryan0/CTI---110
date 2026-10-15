
# Your Name
# Date
# P3HW2 - Employee Pay
# This program calculates an employee's regular pay, overtime pay, and gross pay

# Get employee information
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Determine overtime and calculate pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_rate = pay_rate * 1.5
    overtime_pay = overtime_hours * overtime_rate
else:
    overtime_hours = 0
    overtime_pay = 0

# Calculate regular pay
if hours_worked > 40:
    regular_pay = 40 * pay_rate
else:
    regular_pay = hours_worked * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display results
print("----------------------------------------")
print(f"Employee name: {employee_name}")
print(f"Pay rate: ${pay_rate:.2f}")
print(f"Hours worked: {hours_worked:.1f}")
print(f"Overtime hours: {overtime_hours:.1f}")
print(f"Overtime pay: ${overtime_pay:.2f}")
print(f"Pay for regular hours: ${regular_pay:.2f}")
print(f"Gross pay: ${gross_pay:.2f}")
print("----------------------------------------")