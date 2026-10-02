# John bardaji
# P2HW2 



module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

grades = [module1, module2, module3, module4, module5, module6]

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

print()
print("Lowest grade:", lowest_grade)
print("Highest grade:", highest_grade)
print("Sum of grades:", sum_of_grades)
print("Average of grades:", format(average_grade, ".2f"))