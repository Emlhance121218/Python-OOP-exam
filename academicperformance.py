score = float(input("Enter score: "))

if score >= 90:
    grade = "Excellent"
elif score >= 75:
    grade = "Good"
elif score >= 60:
    grade = "Satisfactory"
else:
    grade = "Needs Improvement"

print(grade)
