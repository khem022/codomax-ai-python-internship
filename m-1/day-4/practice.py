def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def main():
    name = input("Enter student name: ")

    marks = []

    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))

        if mark < 0 or mark > 100:
            print("Invalid marks! Enter a value between 0 and 100.")
            return

        marks.append(mark)

    total = sum(marks)
    percentage = total / len(marks)
    grade = calculate_grade(percentage)

    print("\n----- Student Report -----")
    print("Name:", name)
    print("Marks:", marks)
    print("Total:", total, "/ 500")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)

    if percentage >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")


main()