grades = {}

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Show All Grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        grades[name] = grade
        print("Student added.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in grades:
            new_grade = input("Enter new grade: ")
            grades[name] = new_grade
            print("Grade updated.")
        else:
            print("Student not found.")

    elif choice == "3":
        for name, grade in grades.items():
            print(f"{name}: {grade}")

    elif choice == "4":
        break

    else:
        print("Invalid option.")