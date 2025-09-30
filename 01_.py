# 📖 Student Report Card System

# Fixed subjects (Tuple)
subjects = ("Math", "Science", "English")

# Unique subjects (Set)
unique_subjects = set(subjects)

# Dictionary to store all students
students = {}

# Number of students
num_students = int(input("Enter number of students: "))

# Loop for multiple students
for i in range(num_students):
    print(f"\n--- Student {i+1} ---")
    
    # Variables (string, int)
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    
    # List for marks
    marks = []
    
    # Taking marks input
    for subject in subjects:
        score = float(input(f"Enter marks in {subject}: "))
        marks.append(score)
    
    # Operators (average calculation)
    avg = sum(marks) / len(marks)
    
    # Control Flow (if-else)
    if avg >= 50:
        result = True   # Pass
    else:
        result = False  # Fail
    
    # Dictionary store
    students[name] = {
        "Age": age,
        "Marks": marks,
        "Average": avg,
        "Passed": result
    }

# Final Output
print("\n📊 Report Card Summary:")
for student, data in students.items():
    print(f"\nName: {student}")
    print(f"Age: {data['Age']}")
    print(f"Marks: {data['Marks']}")
    print(f"Average: {data['Average']}")
    print(f"Passed: {data['Passed']}")
