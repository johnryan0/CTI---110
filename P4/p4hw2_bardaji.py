# John Bardaji
# October 29, 2026
# P4HW2 - Employee Pay
# This program calculates and totals regular, overtime, and gross pay
# for multiple employees.

# Pseudocode:
# Set total overtime pay, regular pay, gross pay, and employee count to zero.
# Ask for an employee name.
# While the name is not exactly "Done":
#     Ask for the employee's pay rate and hours worked.
#     If hours worked are greater than 40:
#         Calculate overtime hours as hours worked minus 40.
#         Calculate overtime pay at 1.5 times the pay rate.
#         Calculate regular pay for 40 hours.
#     Otherwise:
#         Set overtime hours and overtime pay to zero.
#         Calculate regular pay for all hours worked.
#     Calculate gross pay as regular pay plus overtime pay.
#     Display the employee's pay information.
#     Add this employee's pay to the running totals.
#     Increase the employee count by one.
#     Ask for the next employee name.
# Display total overtime pay, regular pay, gross pay, and employee count.

total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
employee_count = 0

employee_name = input("Enter employee's name or 'Done' to terminate: ")

while employee_name != "Done":
    pay_rate = float(input("Enter employee's pay rate: "))
    hours_worked = float(input("Enter number of hours worked: "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay

    print("----------------------------------------")
    print(f"Employee name: {employee_name}")
    print(f"Pay rate: ${pay_rate:.2f}")
    print(f"Hours worked: {hours_worked:.1f}")
    print(f"Overtime hours: {overtime_hours:.1f}")
    print(f"Overtime pay: ${overtime_pay:.2f}")
    print(f"Pay for regular hours: ${regular_pay:.2f}")
    print(f"Gross pay: ${gross_pay:.2f}")
    print("----------------------------------------")

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    employee_name = input("Enter employee's name or 'Done' to terminate: ")

print()
print(" totals")
print(f"Total employees entered: {employee_count}")
print(f"Total overtime pay: ${total_overtime_pay:.2f}")
print(f"Total regular pay: ${total_regular_pay:.2f}")
print(f"Total gross pay: ${total_gross_pay:.2f}")