students = {}

# -----------------------------
# Function to calculate grade
# -----------------------------
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"

# -----------------------------
# Add a new student
# -----------------------------
def add_student():
    name = input("Enter student name: ").strip()

    if name in students:
        print("Student already exists!")
        return

    try:
        math = int(input("Enter Math marks: "))
        science = int(input("Enter Science marks: "))
        english = int(input("Enter English marks: "))
    except ValueError:
        print("Please enter valid numbers!")
        return

    total = math + science + english
    average = total / 3
    grade = calculate_grade(average)

    students[name] = {
        "Math": math,
        "Science": science,
        "English": english,
        "Total": total,
        "Average": round(average, 2),
        "Grade": grade
    }

    print("Student added successfully!")

# -----------------------------
# Show all students
# -----------------------------
def show_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for name, data in students.items():
        print(f"\nName    : {name}")
        print(f"Math    : {data['Math']}")
        print(f"Science : {data['Science']}")
        print(f"English : {data['English']}")
        print(f"Total   : {data['Total']}")
        print(f"Average : {data['Average']}")
        print(f"Grade   : {data['Grade']}")

# -----------------------------
# Search a student
# -----------------------------
def search_student():
    name = input("Enter student name to search: ").strip()

    if name in students:
        data = students[name]
        print("\n--- Student Found ---")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("Student not found!")

# -----------------------------
# Update student marks
# -----------------------------
def update_student():
    name = input("Enter student name to update: ").strip()

    if name not in students:
        print("Student not found!")
        return

    try:
        math = int(input("New Math marks: "))
        science = int(input("New Science marks: "))
        english = int(input("New English marks: "))
    except ValueError:
        print("Invalid input!")
        return

    total = math + science + english
    average = total / 3
    grade = calculate_grade(average)

    students[name] = {
        "Math": math,
        "Science": science,
        "English": english,
        "Total": total,
        "Average": round(average, 2),
        "Grade": grade
    }

    print("Student updated successfully!")

# -----------------------------
# Delete a student
# -----------------------------
def delete_student():
    name = input("Enter student name to delete: ").strip()

    if name in students:
        del students[name]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

# -----------------------------
# Show topper
# -----------------------------
def show_topper():
    if not students:
        print("No records available.")
        return

    topper = max(students, key=lambda x: students[x]["Total"])

    print("\n--- Topper ---")
    print(f"Name : {topper}")
    print(f"Total: {students[topper]['Total']}")
    print(f"Grade: {students[topper]['Grade']}")

# -----------------------------
# Main menu
# -----------------------------
while True:
    print("\n===== Student Result Management System =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        show_topper()
    elif choice == "7":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice! Please enter 1-7.")