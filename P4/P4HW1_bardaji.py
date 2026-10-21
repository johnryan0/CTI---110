 # John Bardaji
 # P4HW1 

# Pseudocode:
# Ask how many scores the user wants to enter.
# Keep asking until the user enters at least two scores.
# Create an empty list to store valid scores.
# Repeat once for each score:
#     Ask the user to enter a score.
#     While the score is below 0 or above 100:
#         Tell the user the score is invalid.
#         Ask the user to enter that score again.
#     Add the valid score to the list.
# Find and display the lowest score.
# Remove one occurrence of the lowest score from the list.
# Calculate the average of the remaining scores.
# Determine the letter grade from the average.
# Display the lowest score, modified list, average, and letter grade.

score_count = int(input("How many scores do you want to enter? "))
while score_count < 2:
    print("Enter at least 2 scores so the lowest score can be dropped.")
    score_count = int(input("How many scores do you want to enter? "))

scores_list = []

for score_number in range(1, score_count + 1):
    score = float(input(f"Enter score #{score_number}: "))

    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{score_number} again: "))

    scores_list.append(score)

lowest_score = min(scores_list)
scores_list.remove(lowest_score)
average_score = sum(scores_list) / len(scores_list)

if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Lowest score entered: {lowest_score:.1f}")
print(f"Score List after dropping lowest score: {scores_list}")
print(f"Average of scores in modified list: {average_score:.2f}")
print(f"Letter grade: {letter_grade}")