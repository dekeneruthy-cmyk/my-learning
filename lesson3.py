print("=== PNG Grade Checker ===")

score = float(input("Enter your score (0-100): "))

if score >= 75:
    grade = "A - DISTINCTION!"
elif score >= 65:
    grade = "B - CREDIT!"
elif score >= 50:
    grade = "C - PASS"
else:
    grade = "F - Try again"

print(f"Your grade: {grade}")

if score < 50:
    print("Don't give up, Ruthy! Keep coding!")
else:
    print("You Passed! ")