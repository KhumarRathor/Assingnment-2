# 📘 Assingment 2

This repository contains **4 beginner-friendly Python mini projects** that demonstrate key concepts such as conditionals, dictionaries, and file operations. Ideal for students practicing basic Python logic.

---

## ✅ 1. Grade Checker

### 🔹 Description:
Takes a numerical score as input and prints the corresponding grade using `if-else` statements.

### 🧠 Logic:
- 90 and above: Grade A
- 80–89: Grade B
- 70–79: Grade C
- 60–69: Grade D
- Below 60: Grade F

### 📄 Code:
```python
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)
```

---

## ✅ 2. Student Grades Manager

### 🔹 Description:
Uses a dictionary to store student names and grades. Users can:
- Add new students
- Update grades
- Print all entries

### 📄 Code:
```python
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
```

---

## ✅ 3. Write to a File

### 🔹 Description:
Creates and writes content to a file named `output.txt` using Python's file handling.

### 📄 Code:
```python
file = open("output.txt", "w")
file.write("Hello! This is a test file.\nThis is the second line.")
file.close()
print("File written successfully.")
```

---

## ✅ 4. Read from a File

### 🔹 Description:
Reads the contents from `output.txt` and prints it to the console.

### 📄 Code:
```python
file = open("output.txt", "r")
content = file.read()
print("File content:\n", content)
file.close()
```

---

## 📂 Files in This Project

- `grade_checker.py`
- `student_grades.py`
- `write_file.py`
- `read_file.py`
- `output.txt` (created at runtime)
- `README.md` (this file)

---

## 👨‍💻 BY

**Khumar Rathor**

---
